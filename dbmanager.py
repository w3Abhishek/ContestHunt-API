from supabase import create_client, Client
import time
import os

# Fetch Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

# Supabase Client setup
supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)

def fetch_items(item_type: str, platform: str = None):
    if item_type not in ["hackathons", "contests", "bounties"]:
        raise ValueError("Invalid item type. Must be one of ['hackathons', 'contests', 'bounties']")
    table_name = item_type
    if platform:
        response = supabase.table(table_name).select("*").eq("platform", platform).order("start_time").execute()
    else:   
        response = supabase.table(table_name).select("*").order("start_time").execute()
    return response.data

def update_items(item_type: str, data: list):
    if item_type not in ["hackathons", "contests", "bounties"]:
        raise ValueError("Invalid item type. Must be one of ['hackathons', 'contests', 'bounties']")
    
    table_name = item_type
    current_time = int(time.time())

    for item in data:
        if item["end_time"] < current_time:
            supabase.table(table_name).delete().match({"url": item["url"]}).execute()
            continue

        existing_item = supabase.table(table_name).select("*").eq("url", item["url"]).execute()

        if not existing_item.data:
            supabase.table(table_name).insert(item).execute()
        else:
            pass