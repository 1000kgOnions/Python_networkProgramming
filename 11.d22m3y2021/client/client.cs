using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;

namespace client
{
    class client
    {
        static void Main(string[] args)
        {
            byte[] dl = new Byte[1024];
            Socket sk = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            IPEndPoint ip = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 9999);
            //Kết  nối đến server
            sk.Connect(ip);

            //nhận chuỗi đã kết nối thành công từ server gửi về
            int kt = sk.Receive(dl);
            string dlnhan = Encoding.ASCII.GetString(dl, 0, kt);
            //in ra màn hình
            Console.WriteLine(dlnhan);

            string chuoigui = Console.ReadLine();
            //chuyển đổi thành bytes
            dl = Encoding.ASCII.GetBytes(chuoigui);
            
            sk.Send(dl);
            ////nhận kq phép cộng
            // kt = sk.Receive(dl);
            // dlnhan = Encoding.ASCII.GetString(dl, 0, kt);
            //Console.WriteLine("ket qua phep cong la:"+dlnhan);
            //dừng màn hình
            Console.ReadLine();
            sk.Close();


        }
    }
}
