import cProfile
import pstats

from run import background_tasks

if __name__ == "__main__":
    with cProfile.Profile() as profile:
        background_tasks()

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()
    results.dump_stats("assets/benchmark_result.prof")
