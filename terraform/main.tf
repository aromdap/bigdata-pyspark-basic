provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "big-data-sg" {

  name = "big-data-security-group"

  ingress {
    cidr_blocks = [ "0.0.0.0/0" ]
    protocol = "tcp"
    from_port        = 22
    to_port          = 22
   }
  egress {
     from_port        = 0
     to_port          = 0
     protocol         = "-1"
     cidr_blocks      = ["0.0.0.0/0"]
     ipv6_cidr_blocks = ["::/0"]
  }
 }

resource "aws_ebs_volume" "big-data-volume" {
  availability_zone = "us-east-1a"
  size              = 8

  tags = {
    Name = "udemy-volume"
  }
}

resource "aws_instance" "big-data-vm" {
  ami = "ami-09e67e426f25ce0d7"
  instance_type = "t1.micro"
  key_name = "deployer-key"
  vpc_security_group_ids = ["${aws_security_group.big-data-sg.id}"]   

  tags = {
    "Name" = "udemy-big-data"
  }
}
resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = file("~/.ssh/id_rsa.pub") 
}
