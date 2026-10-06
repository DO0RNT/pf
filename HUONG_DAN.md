# Website Nguyễn Hồng Thái

## Mở website trên máy

1. Giải nén file ZIP.
2. Mở thư mục `nguyen-hong-thai-portfolio`.
3. Nhấp đúp `index.html` để mở bằng Chrome hoặc Edge.

Không cần cài thư viện hay kết nối Internet để hiển thị website. Các liên kết đến mạng xã hội và nguồn tác phẩm cần Internet khi bạn mở chúng.

Bản trực tuyến: https://nguyen-hong-thai.ldapprotocol.chatgpt.site

## Những gì có trong bản xuất

- Bốn trang: Home, Work, About, Contact.
- Toàn bộ mã HTML, CSS và JavaScript.
- Ba dự án luân phiên, có phần giới thiệu, vai trò và thành tựu đang để chỗ trống.
- Ảnh đính kèm trống, trình xem ảnh phóng lớn và khả năng nhúng PDF.
- The Starry Night, Der Wanderer über dem Nebelmeer và chân dung Leonardo da Vinci trong khung gỗ.
- Ba ảnh phong cảnh làm nền trang chủ, được làm mờ và hòa trộn; vùng sau tên và phần giới thiệu sáng hơn để dễ đọc.
- Hiệu ứng xuất hiện, chuyển trang, chuyển dự án và chuyển động nhẹ của khung tranh.
- Giao diện thích ứng với điện thoại và thiết lập giảm chuyển động.

## Thay nội dung cá nhân

Mở `dist/assets/content.js` bằng VS Code hoặc trình soạn thảo văn bản. Sửa phần giới thiệu, kỹ năng, thông tin học vấn, số điện thoại, email, liên kết LinkedIn/GitHub và ba dự án. Các thông tin chưa được cung cấp đang hiển thị `To be added`.

Để thêm ảnh chân dung, đặt ảnh trong `dist/assets` và đổi `portrait: null` thành đường dẫn như `portrait: 'assets/portrait.jpg'`.

Để thay ảnh hoặc PDF của dự án, đặt tệp trong `dist/assets` rồi sửa `attachment` của dự án:

```js
attachment: {
  type: 'image', // Dùng 'pdf' nếu là PDF.
  src: 'assets/du-an-01.jpg',
  alt: 'Mô tả ảnh hoặc tài liệu dự án',
  placeholder: false
}
```

Giao diện nằm trong `dist/assets/styles.css`; hiệu ứng và tương tác nằm trong `dist/assets/site.js`. Tệp `scripts/render-pages.py` tạo lại khung HTML khi cần; chạy từ thư mục gốc bằng `python scripts/render-pages.py`.

## Triển khai ở nơi khác

Đưa toàn bộ nội dung thư mục `dist` lên dịch vụ hosting website tĩnh. Các ảnh và khung gỗ đã được đính kèm trong bản xuất. Nguồn tác phẩm nằm tại `dist/assets/art/SOURCES.md` và mục Artwork credits trên trang chủ.

Bản xuất hỗ trợ mở trực tiếp trên máy bằng đường dẫn `file:`; hiệu ứng chuyển trang nâng cao phụ thuộc khả năng của trình duyệt. Khi thiết bị bật Reduce Motion, website giảm hiệu ứng và chuyển sang duyệt dự án bằng nút điều khiển.

## Ảnh nền trang chủ

Ba ảnh gốc nằm trong `dist/assets/backgrounds`. Có thể điều chỉnh độ mờ, vị trí và cách hòa trộn trong các lớp `.landscape-open`, `.landscape-breeze`, `.landscape-grass` và `.landscape-wash` của `dist/assets/styles.css`. Bản xuất giữ nguyên ảnh và các dấu nguồn có sẵn.
