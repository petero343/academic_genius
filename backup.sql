-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: acgen_db
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add course',6,'add_course'),(22,'Can change course',6,'change_course'),(23,'Can delete course',6,'delete_course'),(24,'Can view course',6,'view_course'),(25,'Can add student',7,'add_student'),(26,'Can change student',7,'change_student'),(27,'Can delete student',7,'delete_student'),(28,'Can view student',7,'view_student'),(29,'Can add user',8,'add_customuser'),(30,'Can change user',8,'change_customuser'),(31,'Can delete user',8,'delete_customuser'),(32,'Can view user',8,'view_customuser'),(33,'Can add result',9,'add_result'),(34,'Can change result',9,'change_result'),(35,'Can delete result',9,'delete_result'),(36,'Can view result',9,'view_result'),(37,'Can add course',10,'add_course'),(38,'Can change course',10,'change_course'),(39,'Can delete course',10,'delete_course'),(40,'Can view course',10,'view_course'),(41,'Can add Teacher',11,'add_teacher'),(42,'Can change Teacher',11,'change_teacher'),(43,'Can delete Teacher',11,'delete_teacher'),(44,'Can view Teacher',11,'view_teacher'),(45,'Can add user',12,'add_customuser'),(46,'Can change user',12,'change_customuser'),(47,'Can delete user',12,'delete_customuser'),(48,'Can view user',12,'view_customuser'),(49,'Can add user',13,'add_adminuser'),(50,'Can change user',13,'change_adminuser'),(51,'Can delete user',13,'delete_adminuser'),(52,'Can view user',13,'view_adminuser');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_students_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_students_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `students_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(6,'students','course'),(8,'students','customuser'),(9,'students','result'),(7,'students','student'),(10,'teachers','course'),(11,'teachers','teacher'),(13,'users','adminuser'),(12,'users','customuser');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-03-17 22:36:35.223474'),(2,'contenttypes','0002_remove_content_type_name','2025-03-17 22:36:35.368241'),(3,'auth','0001_initial','2025-03-17 22:36:35.839400'),(4,'auth','0002_alter_permission_name_max_length','2025-03-17 22:36:35.948129'),(5,'auth','0003_alter_user_email_max_length','2025-03-17 22:36:35.954842'),(6,'auth','0004_alter_user_username_opts','2025-03-17 22:36:35.973316'),(7,'auth','0005_alter_user_last_login_null','2025-03-17 22:36:35.987284'),(8,'auth','0006_require_contenttypes_0002','2025-03-17 22:36:35.990302'),(9,'auth','0007_alter_validators_add_error_messages','2025-03-17 22:36:35.999581'),(10,'auth','0008_alter_user_username_max_length','2025-03-17 22:36:36.013368'),(11,'auth','0009_alter_user_last_name_max_length','2025-03-17 22:36:36.023439'),(12,'auth','0010_alter_group_name_max_length','2025-03-17 22:36:36.053070'),(13,'auth','0011_update_proxy_permissions','2025-03-17 22:36:36.062350'),(14,'auth','0012_alter_user_first_name_max_length','2025-03-17 22:36:36.072984'),(15,'students','0001_initial','2025-03-17 22:36:36.841821'),(16,'admin','0001_initial','2025-03-17 22:36:37.068188'),(17,'admin','0002_logentry_remove_auto_add','2025-03-17 22:36:37.085511'),(18,'admin','0003_logentry_add_action_flag_choices','2025-03-17 22:36:37.100554'),(19,'sessions','0001_initial','2025-03-17 22:36:37.160749'),(20,'students','0002_student_user','2025-03-17 22:36:37.273480'),(21,'teachers','0001_initial','2025-03-17 22:36:38.071001'),(22,'users','0001_initial','2025-03-17 22:36:38.557212'),(23,'users','0002_alter_customuser_options_alter_customuser_managers_and_more','2025-03-18 01:20:01.512835'),(24,'students','0003_remove_student_email_delete_customuser','2025-03-21 20:18:55.553595'),(25,'teachers','0002_remove_teacher_groups_and_more','2025-03-21 20:19:59.368936'),(26,'students','0004_student_class_grade_student_guardian_contact','2025-03-21 23:28:33.072419'),(27,'users','0002_alter_customuser_email','2025-03-24 12:54:17.830586'),(28,'students','0005_student_email_alter_student_guardian_contact','2025-03-24 13:23:11.447602');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3mfsuhtagoaxobvrgt8r2owyixbqiw55','.eJxVizsOwjAQBe_iGkX2bmKvKckZqK1df2SEAAnHFeLuJCgFlG_mzUsF7ksNveVnuCR1VIDq8AuF4zXfN7PNNnzNDtsw97Y8bufVnPbfX1y51bUsCZkBCrpsLIrzk-BoIEom8SVS1jB6AidibGIPjNHSZKwm0Qk9qvcHSKM2zA:1twlWE:NGNxr748wuygmOv-BJNmfIBfWq4brhNlp2g6dncE2a4','2025-03-25 17:23:22.888759'),('aq9wl4nct4z0kavabklcqh9oh1kg4w6n','.eJxVi8sOwiAURP-FtWmAe3nUpf0G12QKNBijJlJWxn-Xmi50NZk5c14ioK0ltJqf4ZLEUThx-N1mxGu-b2CrdfiSfazD1Or6uJ07Oe2_P7mglm7K2RvWKXvAAH5MS87EBG0SWRnB4J7skiJDRMpqjWitc16pRfIo3h8dnDX9:1twOmS:FhBVIRGj_Ac_qFhHyJi8yBAd8lEnsq8U8DCrHsBXaGU','2025-03-24 17:06:36.524989'),('arvjb4g31swiwt523aknggayvjlf1g6n','.eJxVi8sOwiAURP-FtWmAe3nUpf0G12QKNBijJlJWxn-Xmi50NZk5c14ioK0ltJqf4ZLEUThx-N1mxGu-b2CrdfiSfazD1Or6uJ07Oe2_P7mglm7K2RvWKXvAAH5MS87EBG0SWRnB4J7skiJDRMpqjWitc16pRfIo3h8dnDX9:1tvEOq:qUze0rlkZpBl4i97H8TsXSv6GW0Zxg9MJlWmFXmbCUU','2025-03-21 11:49:24.927139'),('h9xc8nq4au8kppkzjnw98sv9cg296yfy','e30:1tv1Et:x9_VdWoqnkNwfWEw7X64cNhTH9fMP7JXLoQIaMZ-LeQ','2025-03-20 21:46:15.003177'),('joh64qduy8wpbucnks790xivh4p6pc1s','e30:1tv64h:b1AdNuLhW6AAUlbUPxOWSz1E8CWZXioMBoCqRNS0QSQ','2025-03-21 02:56:03.775731'),('ppye654oji1hw4wnd2age5qvw1cqeyw6','e30:1tv0rR:Rz4UiFz6FoPPrFam3_wsXn9JRtr1u5wY9QkhCIoozvY','2025-03-20 21:22:01.474717');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_course`
--

DROP TABLE IF EXISTS `students_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students_course` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `code` varchar(10) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_course`
--

LOCK TABLES `students_course` WRITE;
/*!40000 ALTER TABLE `students_course` DISABLE KEYS */;
INSERT INTO `students_course` VALUES (6,'Mathematics','MATH101','Study of numbers, equations, functions, and geometry.'),(7,'English','ENG101','Development of communication skills in reading, writing, and speaking.'),(8,'Chemistry','CHEM101','Study of matter, chemical reactions, and laboratory techniques.'),(9,'Physics','PHYS101','Understanding the fundamental principles governing the universe.'),(10,'Biology','BIO101','Study of living organisms, their structure, and functions.'),(13,'History','HIST101','Exploration of past events and their impact on the present.'),(14,'Business Studies','BUS102','Understanding business concepts, finance, and entrepreneurship.');
/*!40000 ALTER TABLE `students_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_customuser`
--

DROP TABLE IF EXISTS `students_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_customuser`
--

LOCK TABLES `students_customuser` WRITE;
/*!40000 ALTER TABLE `students_customuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `students_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_result`
--

DROP TABLE IF EXISTS `students_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students_result` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `grade` varchar(5) NOT NULL,
  `course_id` bigint NOT NULL,
  `student_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `students_result_course_id_3e649d81_fk_students_course_id` (`course_id`),
  KEY `students_result_student_id_59461af9_fk_students_student_id` (`student_id`),
  CONSTRAINT `students_result_course_id_3e649d81_fk_students_course_id` FOREIGN KEY (`course_id`) REFERENCES `students_course` (`id`),
  CONSTRAINT `students_result_student_id_59461af9_fk_students_student_id` FOREIGN KEY (`student_id`) REFERENCES `students_student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_result`
--

LOCK TABLES `students_result` WRITE;
/*!40000 ALTER TABLE `students_result` DISABLE KEYS */;
INSERT INTO `students_result` VALUES (17,'67',10,34),(18,'89',10,33),(19,'90',10,32),(20,'83',10,31),(22,'86',8,34),(23,'88',8,33),(24,'81',8,32),(25,'92',8,31),(27,'50',7,34),(28,'59',7,33),(29,'92',7,32),(30,'84',7,31),(32,'56',13,34),(33,'57',13,33),(34,'66',13,32),(35,'61',13,31),(37,'50',6,34),(38,'80',6,33),(39,'50',6,32),(40,'61',6,31),(42,'84',9,34),(43,'61',9,33),(44,'53',9,32),(45,'83',9,31);
/*!40000 ALTER TABLE `students_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_student`
--

DROP TABLE IF EXISTS `students_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students_student` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `adm_number` varchar(20) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `class_grade` varchar(10) NOT NULL,
  `guardian_contact` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `adm_number` (`adm_number`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `students_student_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_student`
--

LOCK TABLES `students_student` WRITE;
/*!40000 ALTER TABLE `students_student` DISABLE KEYS */;
INSERT INTO `students_student` VALUES (31,'STU1001ehhd','Alice','Kimani','2005-03-04',2,'3','254'),(32,'STU1002','Brian','Omondi','2006-07-18',3,'1','254'),(33,'STU1003','Catherine','Wanjiru','2005-11-22',4,'1','254'),(34,'STU1004','David','Mwangi','2006-02-09',5,'1','254'),(36,'STU1005','dewe','ee','1111-11-11',NULL,'',''),(37,'STU1006','John','mwangi','2006-02-04',NULL,'',''),(41,'STU1007','PETER','KARIUKI','2003-11-11',33,'',''),(42,'STU1008','comrade','mzee','2003-12-13',40,'','');
/*!40000 ALTER TABLE `students_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers_course`
--

DROP TABLE IF EXISTS `teachers_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers_course` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `code` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers_course`
--

LOCK TABLES `teachers_course` WRITE;
/*!40000 ALTER TABLE `teachers_course` DISABLE KEYS */;
/*!40000 ALTER TABLE `teachers_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers_teacher_assigned_subjects`
--

DROP TABLE IF EXISTS `teachers_teacher_assigned_subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers_teacher_assigned_subjects` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `teacher_id` bigint NOT NULL,
  `course_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `teachers_teacher_assigne_teacher_id_course_id_8c208662_uniq` (`teacher_id`,`course_id`),
  KEY `teachers_teacher_ass_course_id_af74df35_fk_students_` (`course_id`),
  CONSTRAINT `teachers_teacher_ass_course_id_af74df35_fk_students_` FOREIGN KEY (`course_id`) REFERENCES `students_course` (`id`),
  CONSTRAINT `teachers_teacher_ass_teacher_id_53bd61ec_fk_teachers_` FOREIGN KEY (`teacher_id`) REFERENCES `teachers_teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers_teacher_assigned_subjects`
--

LOCK TABLES `teachers_teacher_assigned_subjects` WRITE;
/*!40000 ALTER TABLE `teachers_teacher_assigned_subjects` DISABLE KEYS */;
INSERT INTO `teachers_teacher_assigned_subjects` VALUES (6,15,6),(9,16,7),(10,17,8),(8,21,9),(5,26,6),(7,27,7);
/*!40000 ALTER TABLE `teachers_teacher_assigned_subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser`
--

DROP TABLE IF EXISTS `users_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(20) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `users_customuser_email_6445acef_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser`
--

LOCK TABLES `users_customuser` WRITE;
/*!40000 ALTER TABLE `users_customuser` DISABLE KEYS */;
INSERT INTO `users_customuser` VALUES (1,'pbkdf2_sha256$870000$Fmj11OkNADCTdCKGuWg1E2$5EZFMMuXFbnbuKaiFtB4fOoKJykIOkD740gN7Zy3swY=',NULL,1,'Kariuki1','peter','kariuki','peterkaryukey@gmail.com',1,1,'2025-03-18 01:21:18.521476',''),(2,'pbkdf2_sha256$870000$3qivOOBXjgkjLPcNQbnnGa$apN+d94rTOaciQppfsAJzFgywlbq8EJTnvFCgCXNdpU=',NULL,0,'STU1001','Alice','Johnson','alice@example.com',0,1,'2025-03-18 04:52:16.000000','student'),(3,'pbkdf2_sha256$870000$QA4607vjyMJ1kxtGc8qNd0$4xYW0DkgB4KYoTxeMwj2zU0js9ViCeYL/4EPmeAV58E=','2025-03-24 14:37:26.841633',0,'STU1002','Brian','Smith','brian@example.com',0,1,'2025-03-18 04:52:16.000000','student'),(4,'pbkdf2_sha256$870000$4jcnkg3tKRZoHZYWTWDSDM$QKXLmKu0vhOtt5gzpw9DpoqC7MH2oLZ9vLPSSCqB9FQ=','2025-03-24 15:50:24.720335',0,'STU1003','Catherine','Lee','catherine@example.com',0,1,'2025-03-18 04:52:16.000000','student'),(5,'pbkdf2_sha256$870000$N2Aiq2QBAAsOdyBoEuLrdJ$ezD4UeahvM4OoXblkZujRWUKmKwB6bukfUODagRiZSc=',NULL,0,'STU1004','David','Brown','david@example.com',0,1,'2025-03-18 04:52:16.000000','student'),(6,'pbkdf2_sha256$870000$lfSarUyK4AfBXmcfnoDPD7$g1rfwowu81FYv4tnnIzjAn1bb1KlvMXhilJOfcBHhus=',NULL,0,'STU1005','Evelyn','Davis','evelyn@example.com',0,1,'2025-03-18 04:52:16.000000','student'),(7,'pbkdf2_sha256$870000$o5YwyExp5IsXcOj3rKglE8$T0vjmes3Wri50uA9qZ9P/89Immg5/HLdarqFwXVaz38=','2025-03-24 15:58:01.998764',1,'SCHADMIN','peter','k','peterkaryukey2@gmail.com',1,1,'2025-03-20 09:33:32.646390',''),(10,'pbkdf2_sha256$870000$FgK11H3RuTl8JiwYjipMqv$WYtGrGHcIItz29gLg6sNhhf5FTm4L50KRPctzNHG69M=',NULL,0,'TCH1001','John','Doe','johndoe@example.com',1,1,'2025-03-20 11:00:43.826592','teacher'),(11,'pbkdf2_sha256$870000$kBn4ozMBgG0dFixM9u1B15$sQeTZAlbrMMfo0QVBCQo3FZ2lsCnNHQaMMetlSVfVFY=',NULL,1,'SHINERS','sh','iners','shiners@gmail.com',1,1,'2025-03-21 20:22:13.659874',''),(12,'pbkdf2_sha256$870000$adO7YLzW7rzXoqh0wUkdv5$ILITFEYfiZWnDAjYt15eQt/FJmZ5/q0op6NOHyEmWAo=',NULL,0,'233','John','Kimani','2883.2021@students.com',1,1,'2025-03-24 07:01:04.020448','teacher'),(23,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=','2025-03-24 17:23:22.881363',0,'15','Alicia','Johnson','alicej@example.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(24,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=',NULL,0,'16','Bob','Williams','bobw@example.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(25,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=','2025-03-24 07:59:53.036388',0,'17','Charlie','Brown','charlieb@example.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(26,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=',NULL,0,'18','David','Clark','davidc@example.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(27,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=',NULL,0,'19','Emma','Walker','emmaw@example.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(28,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=',NULL,0,'20','Frank','Lopez','frankl@example.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(29,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=',NULL,0,'21','Grace','Harris','graceh@example.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(30,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=',NULL,0,'22','Henry','Martin','henrym@example.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(31,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=',NULL,0,'23','John','Kimani','2883.221@students.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(32,'pbkdf2_sha256$870000$JrnMOWnEVLYrJAyqNxZxsv$pSA/LMCvG3VkIzfI+8HYCtvA9JA5hBxyBe9lWFcuAUU=',NULL,0,'26','John','Kamau','peterkaryukiiey@gmail.com',1,1,'2025-03-24 10:55:58.000000','teacher'),(33,'pbkdf2_sha256$870000$upObapqUjS9xzTk7oyjd9B$eYm9zqsaaJGvkmuKtTuaWmXrHyWuRmTA339j95x1j90=','2025-03-24 14:01:54.051981',0,'STU1007','John','mwangi','',0,1,'2025-03-24 12:39:27.914883',''),(36,'pbkdf2_sha256$870000$RmbayfrwegC9buqJemGMFO$Ihkmal4S7IZr9TWjLvdQQfFeujMYzaDpXjVU9Sk+mfk=',NULL,0,'@3','mwalimu','mkongwe','rthj@ku.com',1,1,'2025-03-24 14:04:40.689674','teacher'),(40,'pbkdf2_sha256$870000$BDKnUmpcE8YSII0X6EHKN7$YHvscIUIYuYOiX/Qkq5FobuTtZuca427she8VMr/MMg=',NULL,0,'STU1008','comrade','mzee',NULL,0,1,'2025-03-24 14:32:15.280549','');
/*!40000 ALTER TABLE `users_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser_groups`
--

DROP TABLE IF EXISTS `users_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  KEY `users_customuser_groups_group_id_01390b14_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_customuser_gro_customuser_id_958147bf_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `users_customuser_groups_group_id_01390b14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser_groups`
--

LOCK TABLES `users_customuser_groups` WRITE;
/*!40000 ALTER TABLE `users_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser_user_permissions`
--

DROP TABLE IF EXISTS `users_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  KEY `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_customuser_use_customuser_id_5771478b_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser_user_permissions`
--

LOCK TABLES `users_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-24 20:59:28
