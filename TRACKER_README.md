# 🖱️ Keyboard and Mouse Tracker

A Python program that records keyboard and mouse activities and can replay them, similar to TinyTask functionality.

## ✨ Features

- **Record mouse movements, clicks, and scrolls** with precise timing
- **Record keyboard input** (key presses and releases)
- **Replay recorded actions** once or in a continuous loop
- **Save and load recordings** to/from JSON files
- **Real-time control** with function keys
- **Thread-safe operation** for smooth recording and playback

## 🚀 Quick Start

### Installation

1. Install the required dependency:

```bash
pip install pynput
```

2. Run the tracker:

```bash
python keyboard-mouse-tracker.py
```

Or try the demo:

```bash
python demo_tracker.py
```

### Controls

| Key     | Action                   |
| ------- | ------------------------ |
| **1**   | Start/Stop Recording     |
| **2**   | Replay Recording Once    |
| **3**   | Save Recording to File   |
| **4**   | Load Recording from File |
| **5**   | Loop Replay (Continuous) |
| **6**   | Stop Current Replay/Loop |
| **ESC** | Exit Program             |

## 📖 How to Use

### 1. Recording Your Actions

1. Press **1** to start recording
2. Perform mouse movements, clicks, and keyboard input
3. Press **1** again to stop recording

### 2. Replaying Actions

- Press **2** to replay once
- Press **5** to replay continuously in a loop
- Press **6** to stop an ongoing replay

### 3. Saving and Loading

- Press **3** to save current recording to a timestamped JSON file
- Press **4** to load a previously saved recording

## 🎯 Use Cases

- **Automation testing** - Record and replay user interactions
- **Repetitive tasks** - Automate mouse clicks and keyboard input
- **Demonstrations** - Record actions for tutorials
- **Data entry** - Replay form filling sequences
- **Gaming** - Record and replay game actions

## 📁 File Format

Recordings are saved as JSON files with the following structure:

```json
{
  "events": [
    {
      "type": "mouse_move",
      "x": 100,
      "y": 200,
      "timestamp": 0.5
    },
    {
      "type": "mouse_click",
      "x": 100,
      "y": 200,
      "button": "left",
      "pressed": true,
      "timestamp": 1.0
    }
  ],
  "total_events": 50,
  "duration": 10.5,
  "created": "2024-01-15T10:30:00"
}
```

## 🛠️ Technical Details

### Event Types

- **mouse_move** - Mouse cursor movement
- **mouse_click** - Mouse button press/release
- **mouse_scroll** - Mouse wheel scrolling
- **key_press** - Keyboard key press
- **key_release** - Keyboard key release

### Timing Precision

- Events are timestamped with sub-second precision
- Replay maintains original timing between events
- Smooth playback with minimal lag

### Threading

- Recording runs in background threads
- Non-blocking user interface
- Proper cleanup and resource management

## ⚠️ Important Notes

### Permissions

On macOS, you may need to grant accessibility permissions:

1. Go to System Preferences → Security & Privacy → Privacy
2. Select "Accessibility" from the left panel
3. Add your terminal application or Python to the allowed apps

### Security

- Be careful when replaying recordings that contain sensitive data
- Recordings capture all keyboard input including passwords
- Consider the security implications before sharing recording files

### Limitations

- Some special key combinations may not be recorded properly
- System-level shortcuts might interfere with recording
- Performance may vary depending on system load

## 🔧 Troubleshooting

### Common Issues

**"Permission denied" errors:**

- Grant accessibility permissions (macOS/Linux)
- Try running with elevated privileges if needed

**Module not found:**

```bash
pip install pynput
```

**Recording not working:**

- Check if other applications are blocking input capture
- Ensure the program has proper permissions
- Try running from a different terminal

**Playback issues:**

- Make sure no other automation tools are running
- Check system performance and close unnecessary apps
- Verify the recording file is not corrupted

## 📝 Example Usage

```python
# Import the tracker
from keyboard_mouse_tracker import MouseKeyboardTracker

# Create and run tracker
tracker = MouseKeyboardTracker()
tracker.run()
```

## 🤝 Contributing

Feel free to contribute improvements:

- Add new event types
- Improve timing accuracy
- Add GUI interface
- Enhance file formats
- Add configuration options

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Automating!** 🚀
