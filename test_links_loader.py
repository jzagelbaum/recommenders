#!/usr/bin/env python
"""Test script for the new load_links_df function"""

import sys

sys.path.insert(0, "/workspaces/recommenders")

from recommenders.datasets import movielens

# Test loading links data
print("Testing load_links_df function...")
print("-" * 50)

try:
    # Try loading from 100k (should raise error)
    print("\n1. Testing with 100k (should fail)...")
    try:
        links_df = movielens.load_links_df(size="100k")
        print("   ERROR: Should have raised an exception!")
    except ValueError as e:
        print(f"   ✓ Expected error: {e}")

    # Try loading from 1m
    print("\n2. Testing with 1m dataset...")
    links_df = movielens.load_links_df(size="1m")
    print(f"   ✓ Loaded {len(links_df)} links")
    print(f"   Columns: {list(links_df.columns)}")
    print("\n   First 5 rows:")
    print(links_df.head())

    print("\n3. Testing with custom column names...")
    links_df_custom = movielens.load_links_df(
        size="1m", movie_col="movieId", imdb_col="imdb", tmdb_col="tmdb"
    )
    print(f"   ✓ Loaded with custom columns: {list(links_df_custom.columns)}")
    print(links_df_custom.head())

    print("\n" + "=" * 50)
    print("✓ All tests passed!")

except Exception as e:
    print(f"\n✗ Test failed with error: {e}")
    import traceback

    traceback.print_exc()
