from progress_manager import ProgressManager
from StatisticsManager import StatisticsManager 


class DashboardManager:
    def __init__(self,progress_manager: ProgressManager,statistics_manager: StatisticsManager,):
        self.progress_manager = progress_manager
        self.statistics_manager = statistics_manager

    def display(self):
        print("=" * 60)
        print("               BOOKSCRAPE PRO DASHBOARD")
        print("=" * 60)
        print("\n Progress")
        print("-" * 60)
        print(
        f"Books Processed : "
        f"{self.progress_manager.processed_books} / "
        f"{self.progress_manager.total_books}"
    )

        print(
        f"Progress        : "
        f"[{self.progress_manager.progress_bar}] "
        f"{self.progress_manager.percentage:.2f}%"
    )
        print("\n Statistics")
        print("-" * 60)
        print(
            f"Successful Books :"
            f"{self.statistics_manager.successful_books}"
        )
        print(
            f"Failed Books :"
            f"{self.statistics_manager.failed_books}"
        )
        print(
            f"Recovered Books :"
            f"{self.statistics_manager.recovered_books}"
        )
        print(
            f"Retried Books :"
            f"{self.statistics_manager.retried_books}"
        )

        print("\n Rates")
        print("-" * 60)
        print(
            f"Success Rate :"
            f"{self.statistics_manager.success_rate:.2f}%"
        )
        print(
            f"Failure Rate :"
            f"{self.statistics_manager.failure_rate:.2f}%"
        )
        print(
            f"Recovery Rate :"
            f"{self.statistics_manager.recovery_rate:.2f}%"
        )