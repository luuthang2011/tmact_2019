# -*- coding: utf-8 -*-

# DRIVER_SQL = '{SQL Server Native Client 11.0};'
DRIVER_SQL = '{SQL Server};'

# SERVER_SQL = '113.190.253.193,1433\\AZETSRV;'
SERVER_SQL = '222.252.27.8,1433\\AZETSRV;'
DATABASE_SQL = 'CSDLTayBacUAT;'
USER_SQL = 'taybac;'
PASSWORD_SQL = 'techvify@123;'

DATABASE_POSTGRES = 'ks'
USER_POSTGRES = 'postgres'
PASSWORD_POSTGRES = '1'
HOST_POSTGRES = '10.101.3.204'
PORT_POSTGRES = 5432

Rabbit = 'amqp://guest:guest@52.220.224.131:5672/%2f'

Mongo = 'mongodb://fimo:fimo!54321@10.101.3.204:27017/ks'
Mongo_db = "ks"
Mongo_collection = "map_services"

server = '10.101.3.204'
admin = "fimo"
password = "Mrvm3CVEvr8JGet9"

staticAgs = r"E:\SourceCode\tmact_2019\data\connect_information\ArcgisPublishServer.ags"
db = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'

OBJ_CASE = {
        "id_cthao": "ID_CTHao",
        "khoiluonglo": "KhoiLuongLo",
        "id_ctlo": "ID_CTLo",
        "khoiluonghaovl": "KhoiLuongHaoVL",
        "id_ctgieng": "ID_CTGieng",
        "khoiluonggieng": "KhoiLuongGieng",
        "mota_dks": "MoTa_DKS",
        "bieuhien": "BieuHien",
        "goccam_mattruot": "GocCam_MatTruot",
        "huongcam_mattruot": "HuongCam_MatTruot",
        "vitri": "ViTri",
        "tp_doikientao": "TP_DoiKienTao",
        "mucdobieuhien": "MucDoBieuHien",
        "tinhchatdutgay": "TinhChatDutGay",
        "id_diemks": "ID_DiemKS",
        "loaidks": "LoaiDKS",
        "hole_id": "Hole_ID",
        "chieusau": "ChieuSau",
        "ghi_chu": "Ghi_chu",
        "anh": "Anh",
        "bac_dt": "Bac_DT",
        "bacdithuong": "BacDiThuong",
        "bachamluong": "BacHamLuong",
        "banve": "BanVe",
        "baomat": "BaoMat",
        "caodohao": "CaoDoHao",
        "chieudai": "ChieuDai",
        "chubien": "ChuBien",
        "congthuckhoangvat": "CongThucKhoangVat",
        "dacdiem_dc": "Dacdiem_DC",
        "dacdiem_ks": "Dacdiem_KS",
        "danhphap_bd": "DanhPhap_BD",
        "dientich": "DienTich",
        "dientichcam": "DienTichCam",
        "docaogieng": "DoCaoGieng",
        "docaoh": "DoCaoH",
        "docaolo": "DoCaoLo",
        "doituongcam": "DoiTuongCam",
        "doituongdieutra": "DoiTuongDieuTra",
        "donviqd": "DonViQD",
        "donvith": "DonViTH",
        "dosaugieng": "DoSauGieng",
        "dosauhao": "DoSauHao",
        "file_anhnan": "File_AnhNan",
        "gioi": "Gioi",
        "gocnghieng": "GocNghieng",
        "hamluong": "HamLuong",
        "hamluong_tb": "Hamluong_TB",
        "he": "He",
        "hetoado": "HeToaDo",
        "hientrang": "HienTrang",
        "hientranglk": "HientrangLK",
        "hoathach": "HoaThach",
        "id": "ID",
        "id_da": "ID_DA",
        "id_danhphap": "ID_DanhPhap",
        "id_dvtc": "ID_DVTC",
        "id_ks": "ID_KS",
        "id_ks_dikem": "ID_KS_dikem",
        "id_nhomks": "ID_NhomKS",
        "id_tcdcks": "ID_TCDCKS",
        "id_tyle": "ID_Tyle",
        "isdean": "IsDeAn",
        "kh_kv": "Kh_kv",
        "kh_nguyento": "Kh_nguyento",
        "khlt": "KHLT",
        "khlt_bv": "KHLT_BV",
        "khoangvatkhac": "KhoangVatKhac",
        "khuvuc": "KhuVuc",
        "kinhtuyentruc": "KinhTuyenTruc",
        "kyhieukhoangvat": "KyHieuKhoangVat",
        "loai_ks": "Loai_KS",
        "loaicongtacdodien": "LoaiCongTacDoDien",
        "loaicongtacdotruongluc": "LoaiCongTacDoTruongLuc",
        "loaicongtacdotu": "LoaiCongTacDoTu",
        "loaicongtacdoxa": "LoaiCongTacDoXa",
        "loaidutgay": "LoaiDutGay",
        "mucdich": "MucDich",
        "mucdichkhoan": "MucDichKhoan",
        "mucdo_nc": "Mucdo_NC",
        "mucdonghiencuu": "MucDoNghienCuu",
        "muichieu": "MuiChieu",
        "namkt": "NamKT",
        "namnoplt": "NamNopLT",
        "namtc": "NamTC",
        "ngayketthuc": "NgayKetThuc",
        "ngaykhoicong": "NgayKhoiCong",
        "ngayqd": "NgayQD",
        "nguonvon": "NguonVon",
        "nhom": "Nhom",
        "nhomkhoangsan": "NhomKhoangSan",
        "nhomtobd": "NhomToBD",
        "pha": "Pha",
        "phuhetang": "PhuHeTang",
        "phuongkeodai": "PhuongKeoDai",
        "phuongphapdao": "PhuongPhapDao",
        "phuongphapkhoan": "PhuongphapKhoan",
        "phuongvi": "PhuongVi",
        "sh_diem": "SH_Diem",
        "sohieuhaovl": "SoHieuHaoVL",
        "sohieulo": "SoHieuLo",
        "sohieuvanh": "SoHieuVanh",
        "soqd": "SoQD",
        "tacgia": "Tacgia",
        "tap_phan": "Tap_Phan",
        "ten_kv": "Ten_kv",
        "ten_nguyento": "Ten_nguyento",
        "tenbando": "TenBanDo",
        "tenbanvekvdt": "TenBanVeKVDT",
        "tenbaocao": "TenBaoCao",
        "tenbc": "TenBC",
        "tenbv": "TenBV",
        "tendean": "TenDeAn",
        "tendiem": "TenDiem",
        "tendientich": "TenDienTich",
        "tengieng": "TenGieng",
        "tenhetang": "TenHeTang",
        "tenkhoangsan": "TenKhoangSan",
        "tenkhoangvat": "TenKhoangVat",
        "tenks": "TenKS",
        "tenkvcamhdks": "TenKVCamHDKS",
        "tenlk": "TenLK",
        "tenloaibd": "TenLoaiBD",
        "tennguyento": "TenNguyenTo",
        "tenphuche": "TenPhucHe",
        "tento": "TenTo",
        "tenvung": "TenVung",
        "thanhphanth": "ThanhPhanTH",
        "thietdokhoan": "ThietDoKhoan",
        "thong": "Thong",
        "tietdien": "TietDien",
        "tietdienlo": "TietDienLo",
        "toadomienglox": "ToaDoMiengLoX",
        "toadomiengloy": "ToaDoMiengLoY",
        "toadox": "ToaDoX",
        "toadoy": "ToaDoY",
        "toanvanqd": "ToanVanQD",
        "tuoidc": "TuoiDC",
        "tuong": "Tuong",
        "tuyen": "Tuyen",
        "tuyenhao": "TuyenHao",
        "tyle_bd": "Tyle_BD",
        "vitridialy": "ViTriDiaLy",
        "thoigiandt": "ThoiGianDT",
        "x": "X",
        "y": "Y",
        "z": "Z",
        "caodogieng": "CaoDoGieng",
        "chieudai_met": "ChieuDai_met",
        "chieudaituyen": "ChieuDaiTuyen",
        "chieurong": "ChieuRong",
        "chudautu": "ChuDauTu",
        "cqcapphep": "CQCapPhep",
        "cuongdodongdat": "CuongDoDongDat",
        "doanhnghiepkt": "DoanhNghiepKT",
        "donvithanhlap": "DonviThanhLap",
        "donvitn": "DonviTN",
        "donvitn_tl": "DonviTN_TL",
        "donvituvan": "DonViTuVan",
        "giayphepkt": "GiayPhepKT",
        "giaypheptd": "GiayPhepTD",
        "id_bienchat": "ID_BienChat",
        "id_captltn": "ID_CapTLTN",
        "id_dutgay": "ID_DutGay",
        "id_huyen": "ID_Huyen",
        "id_magma": "ID_Magma",
        "id_nhatky": "ID_NhatKy",
        "id_phieuctlo": "ID_PhieuCTLo",
        "id_tinh": "ID_Tinh",
        "id_tramtich": "ID_TramTich",
        "id_tuyenlt": "ID_TuyenLT",
        "id_xa": "ID_Xa",
        "khuvucks": "KhuVucKS",
        "khuvucnc": "KhuVucNC",
        "kyhieuks": "KyhieuKS",
        "kyhieunguyento": "KyHieuNguyenTo",
        "loaida": "LoaiDa",
        "loaids": "LoaiDS",
        "loaihinhcam": "LoaiHinhCam",
        "loaimau": "Loaimau",
        "loaionhiem": "LoaiONhiem",
        "mdnc": "MDNC",
        "mucdo": "Mucdo",
        "mucdobienchat": "MucdoBienChat",
        "nam": "Nam",
        "namxd": "NamXD",
        "ngayks": "NgayKS",
        "nguoiks": "NguoiKS",
        "nguon_tailieu": "Nguon_tailieu",
        "nhomdanhphap": "NhomDanhPhap",
        "objectid": "ObjectID",
        "phamvidongdat": "PhamViDongDat",
        "quimo": "QuiMo",
        "quymo": "QuyMo",
        "rgb_color": "RGB_Color",
        "soqdgiayphep": "SoQDGiayPhep",
        "tainguyen": "TaiNguyen",
        "tap": "Tap",
        "ten_bv": "Ten_BV",
        "tendanhphap": "TenDanhPhap",
        "tends": "TenDS",
        "tenkv": "TenKV",
        "tentuyen": "TenTuyen",
        "thenam": "TheNam",
        "tn_tl": "TN_TL",
        "truluong": "TruLuong",
        "tyle": "Tyle",
        "vitrihanhchinh": "ViTriHanhChinh",
        "id_khoangsannhole": "ID_khoangsannhole"
      }

LIST_SERVICE = {
  "Tbl_FC_BanDoDiaMao": "Lớp bản đồ địa mạo",
  "Tbl_FC_TaiLieuDoTu": "Tài liệu đo từ",
  "Tbl_FC_TaiLieuDoTrongLuong": "Tài liệu đo trọng lượng",
  "Tbl_FC_TaiLieuDoDien": "Tài liệu đo điện",
  "Tbl_FC_TaiLieuDoXa": "Tài liệu đo xạ",
  "Tbl_FC_DiSanDC": "Lớp di sản địa chất",
  "Tbl_FC_Magma": "Lớp thành tạo magma",
  "Tbl_FC_TramTich": "Lớp Trầm tích",
  "Tbl_FC_BienChat": "Lớp biến chất",
  "Tbl_FC_DutGay": "Lớp đứt gãy",
  "Tbl_FC_VanhPhanTanDH": "Lớp vành phân tán địa hoá",
  "Tbl_FC_DiemDiThuongDH": "Lớp điểm dị thường địa hoá",
  "Tbl_FC_VanhPhanTanTS": "Lớp vành phân tán trọng sa",
  "Tbl_FC_DiemDiThuongTS": "Lớp điểm dị thường trọng sa",
  "Tbl_FC_DCTV_DCCT": "Lớp Địa chất thủy văn - công trình",
  "Tbl_FC_VungONhiem": "Lớp Vùng ô nhiễm",
  "Tbl_FC_VungTruotLo": "Lớp Vùng trượt lở",
  "Tbl_FC_VungDongDat": "Lớp Vùng tiềm năng động đất",
  "Tbl_FC_Khoangsannhole": "Lớp Khoáng sản nhỏ lẻ",
  "Tbl_FC_VungTrienVongKhoangSan": "Lớp vùng triển vọng khoáng sản",
  "Tbl_FC_KVCamHDKS": "Lớp Khu vực cấm hoạt động khoáng sản",
  "Tbl_FC_KVDTKhoangSan": "Lớp Khu vực dự trữ khoáng sản",
  "Tbl_FC_DTChiTiet": "Lớp Diện tích chi tiết",
  "Tbl_FC_LoTrinhDC": "Lộ trình địa chất",
  "Tbl_FC_DiemKS": "Điểm khảo sát",
  "Tbl_FC_CTHaoVL": "Công trình hào (vết lộ)",
  "Tbl_FC_CTGieng": "Công trình giếng",
  "Tbl_FC_CTLo": "Công trình lò",
  "Tbl_FC_LoKhoan": "Bảng lỗ khoan",
  "Tbl_FC_DanhPhapBD": "Danh pháp bản đồ",
  "Tbl_FC_KhuDGKS": "Lớp khu đánh giá khoáng sản",
  "Tbl_FC_TQDienTichDG": "Thân quặng diện tích đánh giá",
  "Tbl_FC_KhuTDKS": "Lớp khu thăm dò khoáng sản",
  "Tbl_FC_TQDienTichTD": "Thân quặng diện tích thăm dò",
  "Tbl_FC_VungTrienVongKhoangSanDG": "Khu vực triển vọng đã đánh giá",
  "Tbl_FC_KhuVucTDKhoangSan": "Khu vực hoạt động thăm dò khoáng sản",
  "Tbl_FC_KhuVucKTKhoangSan": "Khu vực hoạt động khai thác khoáng sản",
  "Tbl_FC_DTCChung": "Diện tích chung",
  "Tbl_Tinh": "Ranh giới tỉnh",
  "Tbl_Huyen": "Ranh giới huyện",
  "Tbl_Xa": "Ranh giới xã"
}
