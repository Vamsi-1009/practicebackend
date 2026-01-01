# Curl Practice: Weather API

Try each command in **terminal** AND **browser** to see the difference.

---

## Weather Commands

### 1. Full Weather Report
```bash
curl wttr.in/Visakhapatnam
```

### 2. Current Weather Only
```bash
curl "wttr.in/Visakhapatnam?0"
```

### 3. Compact One-Line Output
```bash
curl "wttr.in/Visakhapatnam?format=3"
```

### 4. Custom Format (Temperature + Humidity + Wind)
```bash
curl "wttr.in/Visakhapatnam?format=%c+%t+%h+%w"
```

### 5. Sunrise and Sunset Times
```bash
curl "wttr.in/Visakhapatnam?format=Sunrise:%S+Sunset:%s"
```

### 6. JSON Output (for Programming)
```bash
curl "wttr.in/Visakhapatnam?format=j1"
```

### 7. Plain Text (No Colors)
```bash
curl "wttr.in/Visakhapatnam?0T"
```

### 8. Weather by Airport Code
```bash
curl wttr.in/vtz
```

---

## Other Locations (Andhra Pradesh)

### 9. Rajahmundry
```bash
curl "wttr.in/Rajahmundry?format=3"
```

### 10. Tadepalligudem
```bash
curl "wttr.in/Tadepalligudem?format=3"
```

### 11. Sompeta
```bash
curl "wttr.in/Sompeta?format=3"
```

### 12. Anakapalli
```bash
curl "wttr.in/Anakapalli?format=3"
```

### 13. Bobbili
```bash
curl "wttr.in/Bobbili?format=3"
```

### 14. Vizianagaram
```bash
curl "wttr.in/Vizianagaram?format=3"
```

### 15. Chinna Merangi
```bash
curl "wttr.in/Chinna+Merangi?format=3"
```

### 16. Compare All Locations (Run in Terminal)
```bash
curl -s "wttr.in/Visakhapatnam?format=%l:+%t" && echo
curl -s "wttr.in/Rajahmundry?format=%l:+%t" && echo
curl -s "wttr.in/Tadepalligudem?format=%l:+%t" && echo
curl -s "wttr.in/Vizianagaram?format=%l:+%t" && echo
```

---

## Moon Phase Commands

### 17. Current Moon Phase
```bash
curl wttr.in/moon
```

### 18. Moon on Specific Date
```bash
curl wttr.in/moon@2025-01-15
```

---

## Curl Options

### 19. View Response Headers
```bash
curl -i "wttr.in/Visakhapatnam?format=3"
```

### 20. Save Output to File
```bash
curl "wttr.in/Visakhapatnam?0" -o weather.txt
```

---

## Format Placeholders Reference

| Code | Meaning     |
|------|-------------|
| %c   | Weather icon |
| %t   | Temperature |
| %h   | Humidity    |
| %w   | Wind        |
| %S   | Sunrise     |
| %s   | Sunset      |
| %l   | Location    |
| %m   | Moon phase  |
