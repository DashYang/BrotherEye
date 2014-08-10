CREATE DATABASE  IF NOT EXISTS `BrotherEye` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `BrotherEye`;
-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: BrotherEye
-- ------------------------------------------------------
-- Server version	5.5.37-0ubuntu0.12.04.1

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
-- Table structure for table `hero_image`
--

DROP TABLE IF EXISTS `hero_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hero_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(65) NOT NULL,
  `content` varchar(205) NOT NULL,
  `url` varchar(200) NOT NULL,
  `md5` varchar(35) NOT NULL,
  `source` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hero_image`
--

LOCK TABLES `hero_image` WRITE;
/*!40000 ALTER TABLE `hero_image` DISABLE KEYS */;
INSERT INTO `hero_image` VALUES (12,'超级英雄一大黑，汉克皮姆其人——回到V1时代寻找失落的历史','\n至于蚁人和黄蜂在早期复仇者的地位是比较奇怪的。是蚁人提出了组队的想法，黄蜂起了复仇者这个名字。他俩的能力很尴尬，队里浩克铁人托尔随便哪个都是强力党，皮姆觉得自卑，研究出了缩小粒子的反向方程，成为Gi','http://imgsrc.baidu.com/forum/w%3D580/sign=7dcafe4d92ef76c6d0d2fb23ad16fdf6/be5783b1cb1349549134c408544e9258d1094a38.jpg','B92262FCB29A0A6C8FFAC771C7092ECB','http://tieba.baidu.com/p/2814441594'),(13,'超级英雄一大黑，汉克皮姆其人——回到V1时代寻找失落的历史','失去能力后的皮姆暂时退隐了一段时间，复仇者一代解散。钢铁侠，蚁人黄蜂托尔全部离队。参与一项演技时所乘的船只被那摩搞坏，黄蜂决定重出江湖。而皮姆因为上次事件的后遗症导致的身体原因不能出战。\n按照惯例，黄','http://imgsrc.baidu.com/forum/w%3D580/sign=2ea7e2479f16fdfad86cc6e6848e8cea/e9abd354564e925858419f829e82d158cdbf4ee9.jpg','FAE94D4A8D7982A90BFC9696463D59B5','http://tieba.baidu.com/p/2814441594'),(14,'透【美国队长】史蒂夫血清失效急速老化，漫威选出新美队','在美国队长#21中，美队被黄爪的触手插入体内被吸出超级士兵血清后，身体急速衰老，目前已是老头状态，对此情况漫威将选出新任美国队长，从复仇者#35封面来看新任美队应该是猎鹰\n','http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C643%3Bap%3D%D5%FD%D2%E5%C1%AA%C3%CB%B0%C9%2C90%2C651/sign=11b268c960d0f703e6b295d438c1324d/5407825494eef01fa188261be2fe9925be317ddc.jpg','DAA3CA202CC8BD848D87A0957AE0E641','http://tieba.baidu.com/p/3148807676'),(15,'【汉化】 复仇者竞技场 Avengers Arena 01 02','内页预览：\n下载地址：\n复仇者竞技场01：\n复仇者竞技场02：\n微博地址：\n','http://imgsrc.baidu.com/forum/w%3D580/sign=5cf2b002d52a60595210e1121836342d/b3cbf5f2b2119313bd83a37b67380cd793238d45.jpg','FDA5A13309AC8F76764BFFD6379693D9','http://tieba.baidu.com/p/3177440343'),(16,'超级英雄的名言','话说明天更好了...\n@ h5m1d120 超人一枚\n','http://imgsrc.baidu.com/forum/w%3D580/sign=a32da3ee8882b9013dadc33b438fa97e/675e297f9e2f070844e9a2c9eb24b899ab01f290.jpg','F744CD2628FAE4400116B3E69F65EE79','http://tieba.baidu.com/p/3172714622'),(17,'自己画的，用来做背景，渣渣画，不喜勿喷。。','\n删了副超人，重新发过\n今天是丧钟的\n','http://imgsrc.baidu.com/forum/w%3D580/sign=79847700533d26972ed3085565fab24f/1297b0096b63f624b20873c98544ebf81b4ca328.jpg','3F7EF3575576791464E004DDD32DC300','http://tieba.baidu.com/p/3165854234'),(18,'【资源】蝙蝠侠新冒险两季24集自制字幕下载','这贴本来是在蝙蝠侠吧首发的，现在24集全部做完发到正吧，也算是11级了给吧友做的贡献吧，之前铭公子也发过但不是全集。本人做这东西全程都是一个人，并没有加入什么字幕组，所以历时两个月才完成，希望大家喜欢','http://imgsrc.baidu.com/forum/w%3D580/sign=79cb93db13dfa9ecfd2e561f52d1f754/a6ab07f790529822f916c804d5ca7bcb0b46d45d.jpg','FA3E07CC1C5B2DD0E84A4A4FE197E938','http://tieba.baidu.com/p/3169561527'),(19,'【黑历史资源】老爷真正的超能力！','在故事<<Batman The Widening Gyre>>里,蝙蝠侠Bruce Wayne把未婚妻Silver.t.Cloud带来见管家阿福.阿尔弗雷德询问为何Silver.t.Cloud称Bru','http://imgsrc.baidu.com/forum/w%3D580/sign=65649f0e08d162d985ee621421dea950/a39e63224f4a20a4214fed0d92529822730ed034.jpg','7025B93CAE0392B63FACCD9EB30F24DD','http://tieba.baidu.com/p/3176135761'),(20,'巫毒你肿么了？','被末日未来的巫毒雷到了，巫毒以前那么好看，而且不是变形能力者么，怎么末日未来会变成那个好像吸了毒一样的女人。。。太TM吓人了吧\n本集还发现一个得罪画师的，这货是谁啊表示没认出来\n','http://imgsrc.baidu.com/forum/w%3D580/sign=a8d155bf41a98226b8c12b2fba83b97a/6b5cbd1c8701a18bc4c3c5859c2f07082938fe5d.jpg','2085E012282C65588A5670098498E39C','http://tieba.baidu.com/p/3176114079');
/*!40000 ALTER TABLE `hero_image` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-08-10 18:48:58
