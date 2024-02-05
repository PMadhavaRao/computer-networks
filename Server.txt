import java.io.*;
import java.net.*;
import java.util.Scanner;
class Write implements Runnable
{
	Socket s;
	Write(Socket s)
	{
		this.s=s;
	}
	public void run()
	{
		try
		{
			Scanner scn = new Scanner(System.in);
			DataOutputStream dos=new DataOutputStream(s.getOutputStream());
			String smessage="";
			while(!smessage.equals("BYE"))
			{
				smessage=scn.nextLine();
				dos.writeUTF(smessage);
			}
                   s.close();
		}
		catch(Exception e)
		{
		}	
	}
}
class Read implements Runnable
{
	Socket s;
	Read(Socket s)
	{
		this.s=s;
	}
	public void run()
	{
		try
		{
			String message="";
			DataInputStream dis=new DataInputStream(s.getInputStream());
			while(!message.equals("BYE"))
			{
				message=dis.readUTF();
				System.out.println("Client says : "+message);
			}
			s.close();
		}
		catch(Exception e)
		{
		}
	}
}
class Server
{
		public static void main(String[] args)
		{
			try
			{
				String message="";
				ServerSocket ss=new ServerSocket(6666);
				System.out.println("Server waiting at port no 6666");
				  
				Socket s=ss.accept(); 
				System.out.println("Client Connected");
				 
				DataInputStream dis=new DataInputStream(s.getInputStream());  
				DataOutputStream dos=new DataOutputStream(s.getOutputStream());  
				
				Read r=new Read(s);
				Write w=new Write(s);
				new Thread(r).start();
				new Thread(w).start();
				
			}
			catch(Exception e)
			{
			}
		}
}
