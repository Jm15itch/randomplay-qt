# randomplay-qt
A python based QT5 application which interacts with [randomplay](https://tracker.debian.org/pkg/randomplay)

## Todo
- [x] Develop base application with functioning interacts with randomplay
- [ ] Provide all options to randomplay via the application
- [ ] Output the stdout of randomplay to a terminal on the application (easy debugging and temporary solution until the next todo is completed)
- [ ] Add console arguments to allow for scripting.
- [ ] Volume controls (most likely implemented using pycaw)
- [ ] Allow the application to read randomplay outputs (list currently playing song etc)
- [ ] Beautify the application (images for buttons, etc)
### Backlog
- [ ] Possibly implement a playlist feature, displaying the next few songs for instance or maybe the chances.
- [ ] Maybe add a history (e.g. previous music folder usage etc)
- [ ] UI customisation

## Build

```
git clone https://github.com/Jm15itch/randomplay-qt
cd randomplay-qt
pip install -r requirements.txt
python3 main.py
```
