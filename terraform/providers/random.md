# Random

## Описание. 
Позволяет сгенерировать какое-то нзвание.

## Поехали!
```
resource "random_pet" "cat" {
  length = 1
  prefix = "mur"
  separator = " "
}
```
```
resource "random_pet" "server" {
  keepers = {
    # Generate a new pet name each time we switch to a new AMI id
    ami_id = var.ami_id
  }
}

resource "random_password" "password" {
  length           = 16
  special          = true
  override_special = "!#$%&*()-_=+[]{}<>:?"
}

resource "aws_db_instance" "example" {
  instance_class    = "db.t3.micro"
  allocated_storage = 64
  engine            = "mysql"
  username          = "someone"
  password          = random_password.password.result
}
```

## Полезные ссылки.
https://github.com/hashicorp/terraform-provider-random/blob/main/examples/provider/provider.tf
