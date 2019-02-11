-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: DB_work
-- ------------------------------------------------------
-- Server version	5.7.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `commentsTable`
--

DROP TABLE IF EXISTS `commentsTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commentsTable` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` varchar(255) DEFAULT NULL,
  `img_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `img_id` (`img_id`),
  CONSTRAINT `commentsTable_ibfk_1` FOREIGN KEY (`img_id`) REFERENCES `imageTable` (`img_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commentsTable`
--

LOCK TABLES `commentsTable` WRITE;
/*!40000 ALTER TABLE `commentsTable` DISABLE KEYS */;
/*!40000 ALTER TABLE `commentsTable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imageTable`
--

DROP TABLE IF EXISTS `imageTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imageTable` (
  `img_path` varchar(255) DEFAULT NULL,
  `img_name` varchar(255) DEFAULT NULL,
  `img_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`img_id`),
  UNIQUE KEY `img_path` (`img_path`,`img_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imageTable`
--

LOCK TABLES `imageTable` WRITE;
/*!40000 ALTER TABLE `imageTable` DISABLE KEYS */;
INSERT INTO `imageTable` VALUES ('/static/pic1.jpg','pic1.jpg',3),('/static/pic2.jpeg','pic2.jpeg',4),('/static/pic3.jpeg','pic3.jpeg',5);
/*!40000 ALTER TABLE `imageTable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-11 20:26:15
