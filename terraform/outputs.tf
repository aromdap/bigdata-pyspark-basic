output "server_ip" {
  value = "${aws_instance.big-data-vm.public_ip}"
}
