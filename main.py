from routes.index import run_app

if __name__ in {"__main__", "__mp_main__"}:
    print("Running app...")
    try:
        run_app()
    except Exception as e:
        print(f"Error: {e}")
        print("App crashed.")
