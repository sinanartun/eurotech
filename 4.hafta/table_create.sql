CREATE TABLE `properties` (
  `property_id` int NOT NULL AUTO_INCREMENT,
  `price` decimal(15,2) DEFAULT NULL,
  `area` int DEFAULT NULL,
  `bedrooms` int DEFAULT NULL,
  `bathrooms` int DEFAULT NULL,
  `stories` int DEFAULT NULL,
  `mainroad` varchar(3) DEFAULT NULL,
  `guestroom` varchar(3) DEFAULT NULL,
  `basement` varchar(3) DEFAULT NULL,
  `hotwaterheating` varchar(3) DEFAULT NULL,
  `airconditioning` varchar(3) DEFAULT NULL,
  `parking` int DEFAULT NULL,
  `prefarea` varchar(3) DEFAULT NULL,
  `furnishingstatus` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`property_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2539930 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;