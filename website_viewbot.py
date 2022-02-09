import webbrowser
print("Views you need")
view = int(input())
print("Put your URL")
url = input()
for x in range(view):
        webbrowser.open(url)
