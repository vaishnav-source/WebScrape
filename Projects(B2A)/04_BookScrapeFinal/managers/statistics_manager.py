class StatisticsManager:
    def __init__(self) -> None :
        self.processed_books = 0
        self.successful_books = 0
        self.failed_books = 0
        self.retried_books = 0
        self.recovered_books = 0

    def record_success(self) -> None:
        """Record a successful book scrape."""
        self.processed_books += 1
        self.successful_books += 1

    def record_failure(self) -> None :
        """Record a failed book scrape."""
        self.processed_books += 1
        self.failed_books += 1

    def record_retry(self) -> None :
        """Record a failed book retry and scrape again."""
        self.retried_books += 1

    def record_retry_success(self) -> None :
        """Record a successful retry after a failed scrape."""
        self.failed_books -= 1
        self.successful_books += 1
        self.recovered_books += 1

    @property
    def success_rate(self) -> float:
        if self.processed_books == 0:
            return 0.0
        return round ( (self.successful_books / self.processed_books) * 100,2)
    
    @property
    def failure_rate(self) -> float:
        if self.processed_books == 0:
            return 0.0
        return round((self.failed_books / self.processed_books) * 100, 2)

    @property
    def recovery_rate(self) -> float :
        total_failed = self.failed_books + self.recovered_books

        if total_failed == 0:
            return 0.0

        return round((self.recovered_books / total_failed) * 100, 2)
        