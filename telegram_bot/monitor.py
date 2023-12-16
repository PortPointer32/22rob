import subprocess

if __name__ == '__main__':
    while True:
        try:
            subprocess.run(["/home/str/22rob/.venv/bin/python", "/home/str/22rob/start_all_bot.py"])
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")
