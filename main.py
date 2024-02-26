import os

from dotenv import load_dotenv

from leetcode_sync import LeetcodeSync

load_dotenv()


def main() -> None:
    # Load configs
    leetcode_session: str = os.getenv('LEETCODE_SESSION')
    csrf_token: str = os.getenv('CSRF_TOKEN')
    if not leetcode_session or not csrf_token:
        raise ValueError('Session is not set')

    # Parse and update recent submissions
    leetcode_sync = LeetcodeSync(csrf_token, leetcode_session)
    leetcode_sync.generate_files()


if __name__ == '__main__':
    main()
