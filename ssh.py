from netmiko import ConnectHandler          #import hàm ConnectHandler từ thư viện Netmiko
R6 = {                                                        #Tạo Dict SW1 bao gồm các thuộc tính như sau
'device_type':'cisco_ios',                               #device_type nếu dùng thiết bị Cisco để cisco_ios
'ip':' 10.215.27.80',                                           #ip của SW
'username':'vnpro',                                        #username là tên truy cập SSH vào Switch
'password':'vnpro#123',                                            #password là password truy cập SSH vào Switch 
'secret':'vnpro#321',                                         #secret là enable password của Switch
}                           
try:
    # Kết nối SSH
    net_connect = ConnectHandler(**R6)
    net_connect.enable()  # Vào chế độ enable

    # Gửi lệnh "show ip interface brief" và in kết quả
    output = net_connect.send_command("show ip interface brief")
    print(output)

    # Ngắt kết nối SSH
    net_connect.disconnect()

except Exception as e:
    print(f"Lỗi: {e}")
