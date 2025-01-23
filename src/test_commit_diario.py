import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import datetime
import requests
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import commit_diario

class TestCommitDiario(unittest.TestCase):

    @patch("commit_diario.requests.get")
    @patch("commit_diario.log_event")
    def test_obter_clima_success(self, mock_log_event, mock_requests_get):
        mock_response = MagicMock()
        mock_response.text = "Blumenau: ☀️ +25°C"
        mock_response.raise_for_status = MagicMock()
        mock_requests_get.return_value = mock_response

        expected_output = f"Local e Clima: Blumenau: ☀️ +25°C\nHora: {datetime.datetime.now()}\n"
        result = commit_diario.obter_clima()

        self.assertIn("Local e Clima: Blumenau: ☀️ +25°C", result)
        mock_requests_get.assert_called_once_with("https://wttr.in/Blumenau?format=%l:+%c+%t")
        mock_log_event.assert_not_called()

    @patch("commit_diario.requests.get")
    @patch("commit_diario.log_event")
    def test_obter_clima_failure(self, mock_log_event, mock_requests_get):
        mock_requests_get.side_effect = requests.RequestException("Error")

        result = commit_diario.obter_clima()

        self.assertEqual(result, "Erro ao obter informações do clima.")
        mock_log_event.assert_called_once_with("Erro ao obter clima: Error")

    @patch("commit_diario.subprocess.run")
    @patch("commit_diario.obter_clima")
    @patch("commit_diario.log_event")
    @patch("builtins.open", new_callable=mock_open)
    @patch("os.chdir")
    def test_adicionar_e_enviar_arquivo(self, mock_chdir, mock_open, mock_log_event, mock_obter_clima, mock_subprocess_run):
        mock_obter_clima.return_value = "Local e Clima: Blumenau: ☀️ +25°C\nHora: 2023-10-10 10:00:00\n"

        commit_diario.adicionar_e_enviar_arquivo()

        mock_chdir.assert_called_once_with(commit_diario.REPO_PATH)
        mock_open.assert_called_once_with(commit_diario.FILENAME, "w", encoding="utf-8")
        mock_open().write.assert_called_once_with("Local e Clima: Blumenau: ☀️ +25°C\nHora: 2023-10-10 10:00:00\n")
        self.assertEqual(mock_subprocess_run.call_count, 4)
        mock_log_event.assert_called_once_with(f"Arquivo {os.path.basename(commit_diario.FILENAME)} adicionado e enviado ao repositório!")

if __name__ == "__main__":
    unittest.main()