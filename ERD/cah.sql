-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema user_schema_cah
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema user_schema_cah
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `user_schema_cah` DEFAULT CHARACTER SET utf8 ;
USE `user_schema_cah` ;

-- -----------------------------------------------------
-- Table `user_schema_cah`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_schema_cah`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `character_name` VARCHAR(255) NULL,
  `hash_pw` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_schema_cah`.`cards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_schema_cah`.`cards` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `card_name` VARCHAR(255) NULL,
  `card_statement` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cards_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_cards_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `user_schema_cah`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;