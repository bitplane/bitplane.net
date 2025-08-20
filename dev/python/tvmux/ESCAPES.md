# TVMux Semantic Annotations via Custom Escape Sequences

This document outlines the design for a semantic annotation system using custom DCS (Device Control String) escape sequences to inject contextual metadata into terminal recordings.

## Overview

The goal is to embed structured, machine-readable annotations into terminal recordings that provide rich semantic context for downstream analysis tools like `bittty`. These annotations are invisible to standard terminal emulators but preserved in asciinema cast files.

## Technical Foundation

### DCS (Device Control String) Format

We use DCS sequences for better terminal compatibility and structured parameter support:

```
ESC P tvmux://event-type?params ESC \
```

**Why DCS over APC:**
- Better terminal emulator support
- Supports structured parameters natively
- Well-established pattern for application-specific protocols
- Properly ignored by standard terminals (invisible)

### URL-Style Routing

The URL format provides:
- **Hierarchical organization** - `tvmux://category/action?params`
- **API-like semantics** - Natural routing and parameter passing
- **Human readability** - Self-documenting event types
- **Extensibility** - Easy to add new event categories

## Event Categories

### Phase 1: Foundation Events (High Priority)

#### Basic Context
```
tvmux://timestamp?unix=1642123456&iso=2024-01-13T15:30:56Z
tvmux://pane?session=main&window=1&pane=2&active=true
tvmux://process?pid=12345&cmd=vim&args=file.txt&ppid=12300
```

#### Manual Annotations
```
tvmux://note?text=debugging%20auth%20issue&category=work&priority=high
tvmux://bell?from=main:1:3&reason=build_complete&urgent=false
```

#### System Events
```
tvmux://clipboard?action=copy&length=42&hash=sha256:abc123
tvmux://notification?app=slack&title=Message%20from%20Alice&urgent=false
```

### Phase 2: Shell Integration (Medium Priority)

#### Command Lifecycle
```
tvmux://command/start?cmd=grep&args=-r%20pattern%20.&pid=12345&cwd=/home/user/project
tvmux://command/end?cmd=grep&exit_code=0&duration=1.2s&output_lines=15
tvmux://search/history?query=git%20log&matches=15&selected=git%20log%20--oneline
```

#### Context Changes
```
tvmux://cwd?from=/home/user&to=/home/user/project&method=cd
tvmux://git?branch=feature-xyz&repo=myproject&dirty=true&ahead=2&behind=0
tvmux://env?var=NODE_ENV&value=development&previous=production
```

### Phase 3: Advanced Integration (Lower Priority)

#### Content & References
```
tvmux://link?url=https://example.com&context=opened_from_terminal&title=Example%20Site
tvmux://file?path=/etc/passwd&hash=sha256:abc123&semantic_id=config_file_123&type=system_config
tvmux://manpage?page=grep&section=1&context=referenced&query=regular%20expressions
```

#### Voice & Deferred Notes
```
tvmux://voice/start?note_id=uuid123&duration_estimate=30s&trigger=hotkey
tvmux://voice/end?note_id=uuid123&transcription_pending=true&duration=28.5s
tvmux://voice/transcribed?note_id=uuid123&text=remembered%20to%20fix%20auth%20bug&language=en
```

#### Advanced Context
```
tvmux://search/web?query=python%20async%20patterns&engine=google&results_count=10
tvmux://download?url=https://releases.ubuntu.com/file.iso&size=3.2GB&destination=/tmp
tvmux://package?action=install&name=nginx&manager=apt&version=1.18.0
```

## Implementation Strategy

### Phase 1: Core Infrastructure (Week 1)

1. **DCS Sequence Utilities**
   ```python
   def encode_tvmux_annotation(event_type: str, **kwargs) -> str:
       """Encode semantic data as DCS sequence with URL format"""

   def write_annotation_to_fifo(fifo_path: Path, event_type: str, **kwargs):
       """Write annotation to recording stream"""

   def parse_tvmux_annotation(dcs_string: str) -> Dict[str, Any]:
       """Parse DCS back into structured data for analysis"""
   ```

2. **Configuration System**
   ```toml
   [annotations]
   enabled = true
   format = "url"  # Future: support json, keyvalue
   timestamp_all_events = true

   [annotations.events]
   timestamp = true
   pane = true
   process = true
   note = true
   bell = true
   clipboard = false      # Privacy-sensitive, off by default
   notification = false   # Off by default

   [annotations.clipboard]
   max_length = 100
   hash_content = true

   [annotations.notification]
   apps = ["slack", "discord"]  # Whitelist specific apps
   urgent_only = true
   ```

3. **Integration Points**
   - Pane switching in `_dump_pane()`
   - Tmux hook callbacks for system events
   - Recording start/stop events

### Phase 2: Shell Integration (Weeks 2-3)

1. **PS1 Integration** - Detect context changes via prompt hooks
2. **Command Wrappers** - Override common commands with annotation functions:
   ```bash
   # Shell function wrapper example
   original_grep() { command grep "$@"; }
   grep() {
       echo -e "\ePtvmux://command/start?cmd=grep&args=$(url_encode "$*")\e\\"
       local start_time=$(date +%s.%N)
       local exit_code
       original_grep "$@"
       exit_code=$?
       local duration=$(echo "$(date +%s.%N) - $start_time" | bc)
       echo -e "\ePtvmux://command/end?cmd=grep&exit_code=$exit_code&duration=${duration}s\e\\"
       return $exit_code
   }
   ```

3. **Directory Change Detection** - Hook `cd`, `pushd`, `popd`
4. **Git Branch Monitoring** - PS1 integration + git command wrappers

### Phase 3: Advanced Features (Week 4+)

1. **Desktop Integration**
   - D-Bus monitoring for notifications (`org.freedesktop.Notifications`)
   - X11/Wayland clipboard event detection
   - XDG desktop file associations

2. **Voice Notes System**
   - Hotkey integration (tmux key binding)
   - Audio recording to temporary files
   - Whisper transcription pipeline
   - Note ID linking and resolution

3. **TUI Application Hooks**
   - LD_PRELOAD wrapper for ncurses functions
   - Python decorators for textual applications
   - Semantic markup injection at interaction points

## Configuration Examples

### Basic Setup (Privacy-Focused)
```toml
[annotations]
enabled = true

[annotations.events]
timestamp = true
pane = true
process = true
note = true
# All system integration disabled for privacy
clipboard = false
notification = false
command = false
```

### Full Development Setup
```toml
[annotations]
enabled = true
timestamp_all_events = true

[annotations.events]
timestamp = true
pane = true
process = true
note = true
bell = true
command = true
cwd = true
git = true
clipboard = true
notification = true

[annotations.clipboard]
enabled = true
max_length = 200
hash_long_content = true

[annotations.notification]
enabled = true
apps = ["slack", "discord", "teams"]
urgent_only = false
include_body = false  # Privacy
```

## Use Cases & Benefits

### For bittty Terminal Player
- **Rich Timeline Navigation** - "Show me when I started debugging"
- **Context-Aware Search** - "Find all grep commands that failed"
- **Semantic Replay** - "Replay from when I switched to this directory"
- **Enhanced Visualization** - Command success/failure overlays, process trees
- **Smart Bookmarking** - Automatic identification of interesting moments

### For Analysis & Documentation Tools
- **Automated Workflow Documentation** - Generate tutorials from recorded sessions
- **Performance Analysis** - Command timing with full context
- **Learning Pattern Extraction** - Identify common workflows and pain points
- **RAG Database Integration** - Semantic search across terminal history
- **Debugging Session Analysis** - Track problem-solving approaches

### For AI Training & Assistance
- **Rich Context for Code Generation** - Understand current development context
- **Workflow Understanding** - Learn from actual developer workflows
- **Error Pattern Recognition** - Identify common failure modes and solutions
- **Context-Aware Help** - Provide suggestions based on current activity

## Technical Considerations

### Performance
- **Lazy Evaluation** - Only generate annotations when recording is active
- **Efficient Encoding** - Minimal overhead for DCS sequence generation
- **Configurable Filtering** - Disable expensive annotations when not needed
- **Batch Processing** - Group related annotations to reduce I/O

### Privacy & Security
- **Opt-in Everything** - All system integration features disabled by default
- **Content Filtering** - Hash or truncate sensitive data
- **Granular Controls** - Per-application, per-event-type configuration
- **Local Processing** - No external API calls required

### Compatibility
- **Terminal Agnostic** - DCS sequences ignored by standard terminals
- **Graceful Degradation** - System works without annotations
- **Forward Compatibility** - URL format extensible without breaking parsers
- **Version Handling** - Include format version in sequences for future changes

## Future Extensions

### Advanced Semantic Analysis
- **Code Context Detection** - Programming language, framework identification
- **Error Classification** - Automatic categorization of failures
- **Intent Recognition** - Infer user goals from command patterns
- **Cross-Session Correlation** - Link related activities across recordings

### Integration Ecosystem
- **IDE Integration** - Sync with editor state and breakpoint information
- **Browser Integration** - Track research and documentation workflows
- **Issue Tracker Integration** - Link terminal work to tickets/issues
- **Communication Tools** - Context from Slack, email, etc.

---

This design provides a foundation for incredibly rich, semantically-aware terminal recordings that could revolutionize how we analyze, replay, and learn from terminal sessions. The URL-based approach offers familiar semantics while maintaining extensibility and human readability.
