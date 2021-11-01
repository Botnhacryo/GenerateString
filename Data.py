from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Xin chào {}

Chào mừng {}

Nếu bạn không tin vào bot này,
1) Đừng đọc tin nhắn này
2) Chặn bot hoặc xóa trò chuyện

Bot này hoạt động để giúp bạn nhận được chuỗi phiên thông qua Bot. Khuyến nghị Nếu Bạn Muốn Lấy Chuỗi Sử Dụng Tài Khoản Khác, Để Không Bị Trì Hoãn. Cảm ơn bạn
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Bắt đầu tạo phiên 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Trở lại 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Bắt đầu tạo phiên 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Bắt đầu tạo phiên 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Duy trì bởi ✨", url="https://t.me/rimuru737")],
        [
            InlineKeyboardButton("Làm thế nào để sử dụng tôi ❔", callback_data="help"),
            InlineKeyboardButton("🎪 Về bot 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Kênh Group ♥", url="https://t.me/yeusex")],
    ]

    # Help Message
    HELP = """
✨ **Các lệnh có sẵn** ✨

/about - Thông tin về bot
/help - Trợ giúp
/start - Khởi động Bot
/generate - Bắt đầu tạo phiên
/cancel - Hủy bỏ quá trình
/restart - Hủy bỏ quá trình
"""

    # About Message
    ABOUT = """
**About This Bot** 

Một bot điện tín để truy xuất các bản ghi âm và các phiên chuỗi telethon của @rimuru737

Group Support : [Yêu Sex](https://t.me/yeu69)

Channel Support : [Yêu 69](https://t.me/yeusex)
    """
