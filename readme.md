
``` bash
python -m venv venv
./venv/Scripts/Activate.ps1
python -m pip install python-dotenv discord.py requests python-a2s

# linux
sudo apt-get install python3-venv
python3 -m venv venv
./venv/bin/activate
```

# TODO:
[ ] Asynch/await
[ ] Auto discover server list

# readme

**Giới thiệu qua về server Discord này**
- Server được lập với mục đích giúp cộng đồng người chơi Squad nói tiếng việt liên lạc với nhau trước/trong và sau ván game. Trong tương lai nếu có đủ người chơi thì có thể tiến tới tạo Clan chính thức cũng như server game Squad riêng.
- Tự do phát ngôn, nhưng đảm bảo những nguyên tắc trong giao tiếp giống như ngoài đời sống thực [netiquette](https://en.wikipedia.org/wiki/Etiquette_in_technology). Không có chỗ cho mạt sát chửi bới người chơi khác. Không nên thảo luận những chủ đề không liên quan đến game trong channel chung. 
- [WIP]

**Tính năng**:

_Voice channels_
- Admin đã tạo sẵn một số server mà ae thường chơi để tiện trao đổi cho những người chơi cùng server. Join server dành cho squad để trao đổi nội bộ trong squad nếu số lượng người join quá đông gây nhiễu. 
- Tại sao chúng ta lại cần voice channel trong khi Squad đã có sẵn voice:
    + Trong squad chỉ có 2 người Việt, còn lại là English speaking boys.
    + Squad toàn người Việt nhưng lười bấm "B".
    + Ae chơi ở các squad khác khau (Mortar, Heli, ...) cần Squad leader roll.
    + Chưa kể dùng voice channel sẽ tiện để mọi người biết ae đang chơi server nào để còn vào chơi cùng, hỏi chơi team nào squad nào, unlock squad, invite, ...

_Text channel_ #server-status
- Một script python sẽ liên tục query những server ae thường chơi để liệt kê những thông tin như Map, Mode, players ... và quan trọng nhất là **liệt kê tên thành viên đang chơi**. Nếu bạn không muốn bị liệt kê bởi Bot này thì chỉ việc nói với Mod để cập nhật.

**Đóng góp ý kiến**:
- Mọi ý kiến và chỉ trích đều được hoan nghênh. Ae có thể viết trên channel chung hoặc gửi tin nhắn riêng.
- Chúng tôi đang cần tham khảo ý kiến phát triển server Discord: Thêm channel, thêm chức năng, Bot, ...


**Note**
- Mute #server-status vì trong đó Bot sẽ post thông tin tự động.