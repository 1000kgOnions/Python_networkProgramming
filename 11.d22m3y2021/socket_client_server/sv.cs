using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace server
{
    class Program
    {
        static void Main(string[] args)
        {
            byte[] dl = new byte[1024];
            int kt;
            Socket sk = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            IPEndPoint ip = new IPEndPoint(IPAddress.Any,9999);
            //gắn socket với IPEndPoint
            sk.Bind(ip);
            //luôn luôn lắng nghe
            sk.Listen(10);
            Console.WriteLine("Dang cho ket noi voi server");
            //accept
            //tạo socket mới,mọi trao đổi thực hiển ở socket mới này
            Socket client = sk.Accept();
            IPEndPoint clientEndPoint = (IPEndPoint)client.RemoteEndPoint;
            //in ra thông tin của client
            Console.WriteLine("ket noi cong:" + clientEndPoint.Address + clientEndPoint.Port);
            //gửi thông điệp đã kết nối dc về client
            string stt = "Da ket noi thanh cong";
            //chuyen string về các byte
            dl = Encoding.ASCII.GetBytes(stt);
            client.Send(dl, dl.Length, SocketFlags.None);

            //nhận từ client
            kt = client.Receive(dl);
            //chuyển đổi thành string
            Random rd = new Random();
            string dlnhan = Encoding.ASCII.GetString(dl, 0, kt);
            if(dlnhan=="SOSO")
            {
                int so = rd.Next(99);
                dl = Encoding.ASCII.GetBytes(so + "");
                client.Send(dl, dl.Length, SocketFlags.None);
            }    
            else
            {
                string[] str = dlnhan.Split(' ');
                int so1, so2, so3;
                so1 = rd.Next(99);
                so2 = rd.Next(99);
                so3 = rd.Next(99);
                string chuoi = so1 + " " + so2 + " " + so3;
                dl = Encoding.ASCII.GetBytes(chuoi);
                client.Send(dl, dl.Length, SocketFlags.None);

            }

            /* 
            //tinh a+b
            //string[] str = dlnhan.Split('+');
            //int kq = Convert.ToInt32(str[0]) + Convert.ToInt32(str[1]);
            ////in ra màn hình
            //Console.WriteLine("ket qua la:"+kq);
            ////gửi ket qua 
            //dl = Encoding.ASCII.GetBytes(kq + "");
            //client.Send(dl);
            */



            //dừng màn hihf và đóng kết nói
            Console.ReadLine();
            sk.Close();

        }
    }
}
