def solution(m, musicinfos):
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    candidates = []
    for musicinfo in musicinfos:
        start, end, title, info = musicinfo.split(",")
        info = info.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        hour1, minute1 = map(int, start.split(":"))
        hour2, minute2 = map(int, end.split(":"))
        time = (60 * hour2 + minute2) - (60 * hour1 + minute1)
        length = len(info)
        song = info * (time // length) + info[:time % length]
        if m in song:
            candidates.append((title, time))
    if candidates:
        candidates.sort(key=lambda x: -x[1])
        answer = candidates[0][0]
    else:
        answer = "(None)"
    return answer
