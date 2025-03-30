import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from app import TumorDetectorGUI


if __name__ == "__main__":
    
    tumor_detector = TumorDetectorGUI()
    tumor_detector.window()