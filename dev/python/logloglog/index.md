# 🪵🪵🪵

![log](log.webp)

> What rolls down stairs, alone or in pairs, and over your neighbor's dog?
> What's great for a snack, And fits on your back?
> It's Log Log Log!

I needed line wrapping in my tty with fast access, so why not make a log that
supports egregious sizes and low seek times?

## ⏩

```bash
# makes log.log.log from /var/log
make log
```

## TODO

- [ ] Textual demo
  - [x] stats in window
  - [ ] slim demo down
  - [x] follow last line when at end
- [x] Async/non-blocking design
  - [x] Make log processing async to avoid blocking
  - [x] Support streaming updates
- [ ] Multiple display backends
- [ ] Python logging integration
  - [ ] Direct logger handlers
  - [ ] Log level filtering and formatting
- [ ] Cache management
  - [ ] Periodic cleanup of cache directories
  - [ ] Check file existence by inode lookup
  - [ ] Handle file rotation and moves

