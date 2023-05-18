import subprocess

# Danh sách các địa chỉ IP cần ping
ip_addresses = ["192.168.0.1", "google.com", "yahoo.com"]

# Hàm thực hiện ping một địa chỉ IP
def ping(ip_address):
    try:
        output = subprocess.check_output(["ping", "-c", "4", ip_address])  # Thực hiện lệnh ping với 4 gói tin
        print(f"Ping {ip_address} thành công!")
        print(output.decode())  # In kết quả ping ra màn hình
    except subprocess.CalledProcessError:
        print(f"Ping {ip_address} thất bại!")

# Thực hiện ping cho từng địa chỉ IP trong danh sách
for ip in ip_addresses:
    ping(ip)
