import java.util.Scanner;
import java.io.*;
import java.net.*;
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
				System.out.println("Server says : "+message);
			}
			s.close();
		}
		catch(Exception e)
		{
		}
	}
}
class Clients
{
	public static void main(String[] args)
	{
		try
		{
			Socket s=new Socket("172.16.6.48",6666);
			String message="";
			System.out.println("Connected To Server");
			Scanner scn=new Scanner(System.in);
			System.out.println("Enter the message");
		
			DataOutputStream dos=new DataOutputStream(s.getOutputStream());  
			DataInputStream dis=new DataInputStream(s.getInputStream()); 
			
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
