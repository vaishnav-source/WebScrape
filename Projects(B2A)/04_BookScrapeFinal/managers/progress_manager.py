import time


class ProgressManager:
    """
    Manages scraping progress, timing, speed, ETA,and renders a progress dashboard."""

    def __init__(self, total_books: int):
        """
        Initialize the Progress Manager.

        Args:
            total_books (int): Total number of books to scrape.
        """

        # Total number of books that will be processed.
        self.total_books = total_books

        # Number of books completed so far.
        self.completed_books = 0

        # Store the start time of the scraping process.
        self.start_time = time.time()

    def update(self) -> None:
        """
        Increment the completed book count.

        Call this once after processing each book.
        """
        self.completed_books += 1

    @property
    def percentage(self) -> float:
        """
        Return scraping completion percentage.
        """

        if self.total_books == 0:
            return 0.0

        return (self.completed_books / self.total_books) * 100

    @property
    def elapsed_time(self) -> float:
        """
        Return elapsed scraping time in seconds.
        """

        return time.time() - self.start_time

    @property
    def speed(self) -> float:
        """
        Return scraping speed in books per second.
        """

        elapsed = self.elapsed_time

        if elapsed == 0:
            return 0.0

        return self.completed_books / elapsed

    @property
    def eta(self) -> float:
        """
        Estimate remaining time in seconds.
        """

        if self.speed == 0:
            return 0.0

        remaining_books = self.total_books - self.completed_books

        return remaining_books / self.speed

    def format_time(self, seconds: float) -> str:
        """
        Convert seconds into HH:MM:SS format.

        Example:
            3665 -> 01:01:05
        """

        seconds = int(seconds)

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        return f"{hours:02}:{minutes:02}:{seconds:02}"

    @property
    def progress_bar(self) -> str:
        """
        Return a visual progress bar. """
        
        width = 30

        filled = int((self.percentage / 100) * width)

        empty = width - filled

        return "█" * filled + "░" * empty

    def render(self) -> str:
        """
        Build the progress dashboard.

        Returns:
            str: Formatted dashboard string.
        """

        # Store calculated values once.
        percentage = self.percentage
        speed = self.speed
        elapsed = self.elapsed_time
        eta = self.eta
        bar = self.progress_bar

        return (
            f"{'=' * 60}\n"
            f"              BookScrape Pro V3\n"
            f"{'=' * 60}\n\n"
            f"Progress : {bar} {percentage:.1f}%\n"
            f"Books    : {self.completed_books}/{self.total_books}\n"
            f"Speed    : {speed:.2f} books/sec\n"
            f"Elapsed  : {self.format_time(elapsed)}\n"
            f"ETA      : {self.format_time(eta)}\n\n"
            f"{'=' * 60}"
        )

    def display(self) -> None:
        """
        Display the dashboard in the terminal.

        Clears the terminal before printing so the
        dashboard updates in-place instead of scrolling.
        """

        # ANSI escape codes:
        # \033[2J -> Clear terminal
        # \033[H  -> Move cursor to top-left
        print("\033[2J\033[H", end="")

        print(self.render())