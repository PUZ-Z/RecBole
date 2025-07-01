from recbole.trainer import KGTrainer
import torch

class LossEarlyStopTrainer(KGTrainer):
    def __init__(self, config, model):
        super().__init__(config, model)
        self.best_valid_loss = float('inf')
        self.stop_counter = 0
        self.stopping_step = config['stopping_step']

    def _valid_epoch(self):
        """Override to calculate validation loss instead of metric."""
        self.model.eval()
        with torch.no_grad():
            total_loss = 0
            for batch_idx, interaction in enumerate(self.valid_data):
                interaction = interaction.to(self.device)
                losses = self.model.calculate_loss(interaction)
                if isinstance(losses, tuple):
                    loss = sum(losses)
                else:
                    loss = losses
                total_loss += loss.item()
        avg_loss = total_loss / len(self.valid_data)
        return avg_loss

    def fit(self, train_data, valid_data):
        self._build_train_loss()
        self.valid_data = valid_data
        for epoch_idx in range(self.start_epoch, self.epochs + 1):
            train_loss = self._train_epoch(train_data, epoch_idx)
            valid_loss = self._valid_epoch()

            self.logger.info(f"Epoch {epoch_idx} - train_loss: {train_loss:.4f} valid_loss: {valid_loss:.4f}")

            if valid_loss < self.best_valid_loss:
                self.best_valid_loss = valid_loss
                self.stop_counter = 0
                self._save_checkpoint(epoch_idx)
            else:
                self.stop_counter += 1

            if self.stop_counter >= self.stopping_step:
                self.logger.info(f"Early stopping at epoch {epoch_idx} based on validation loss.")
                break

        self._restore_checkpoint()