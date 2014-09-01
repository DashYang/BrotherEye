DROP TABLE IF EXISTS `reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reply` (
  `comment_id` varchar(12) NOT NULL,
  `belongto` varchar(12) DEFAULT NULL,
  `content` varchar(600) DEFAULT NULL,
  `user_id` varchar(12) DEFAULT NULL,
  `now_time` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


-- Dump completed on 2014-08-22 16:11:26
