-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 23, 2020 at 03:24 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `parkingsystemdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user_detail', 7, 'add_user_detail'),
(26, 'Can change user_detail', 7, 'change_user_detail'),
(27, 'Can delete user_detail', 7, 'delete_user_detail'),
(28, 'Can view user_detail', 7, 'view_user_detail'),
(29, 'Can add user_ location', 8, 'add_user_location'),
(30, 'Can change user_ location', 8, 'change_user_location'),
(31, 'Can delete user_ location', 8, 'delete_user_location'),
(32, 'Can view user_ location', 8, 'view_user_location'),
(33, 'Can add land_detail', 9, 'add_land_detail'),
(34, 'Can change land_detail', 9, 'change_land_detail'),
(35, 'Can delete land_detail', 9, 'delete_land_detail'),
(36, 'Can view land_detail', 9, 'view_land_detail'),
(37, 'Can add land_record', 10, 'add_land_record'),
(38, 'Can change land_record', 10, 'change_land_record'),
(39, 'Can delete land_record', 10, 'delete_land_record'),
(40, 'Can view land_record', 10, 'view_land_record');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'Landlord', 'land_detail'),
(10, 'Landlord', 'land_record'),
(6, 'sessions', 'session'),
(7, 'User', 'user_detail'),
(8, 'User', 'user_location');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'User', '0001_initial', '2020-04-22 12:42:29.616117'),
(2, 'Landlord', '0001_initial', '2020-04-22 12:42:31.106444'),
(3, 'User', '0002_user_location', '2020-04-22 12:42:34.961146'),
(4, 'contenttypes', '0001_initial', '2020-04-22 12:42:36.620500'),
(5, 'auth', '0001_initial', '2020-04-22 12:42:39.524908'),
(6, 'admin', '0001_initial', '2020-04-22 12:42:48.648921'),
(7, 'admin', '0002_logentry_remove_auto_add', '2020-04-22 12:42:50.573751'),
(8, 'admin', '0003_logentry_add_action_flag_choices', '2020-04-22 12:42:50.612064'),
(9, 'contenttypes', '0002_remove_content_type_name', '2020-04-22 12:42:52.887665'),
(10, 'auth', '0002_alter_permission_name_max_length', '2020-04-22 12:42:54.100930'),
(11, 'auth', '0003_alter_user_email_max_length', '2020-04-22 12:42:54.249604'),
(12, 'auth', '0004_alter_user_username_opts', '2020-04-22 12:42:54.304677'),
(13, 'auth', '0005_alter_user_last_login_null', '2020-04-22 12:42:55.091357'),
(14, 'auth', '0006_require_contenttypes_0002', '2020-04-22 12:42:55.124186'),
(15, 'auth', '0007_alter_validators_add_error_messages', '2020-04-22 12:42:55.170678'),
(16, 'auth', '0008_alter_user_username_max_length', '2020-04-22 12:42:55.298525'),
(17, 'auth', '0009_alter_user_last_name_max_length', '2020-04-22 12:42:55.482187'),
(18, 'auth', '0010_alter_group_name_max_length', '2020-04-22 12:42:55.617316'),
(19, 'auth', '0011_update_proxy_permissions', '2020-04-22 12:42:55.669998'),
(20, 'sessions', '0001_initial', '2020-04-22 12:42:55.982863');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0busssiiiw5gbn7v0eac7cb5p0qxjw8v', 'MWEwZGY1YmQ3NWRmM2I2MTdlMmU5N2I0YWRkNDNmNTQ4ODVkYjg1ZDp7InVpZCI6NCwiZGF0ZSI6IjIwMjAtMDQtMjgiLCJyb2xlIjoiVXNlciIsImVtYWlsMSI6IlNodWJoYW12ZWthcml5YTQwMkBnbWFpbC5jb20ifQ==', '2020-05-07 11:26:25.246294'),
('5ms7s2hxzzk3l696omxetqacika5vzov', 'ZDE2N2FkNTI0N2NlMmNkNTBlZmUxNDhmYjRmNmJlMDc4NGNjMDFiNjp7InJvbGUiOiJVc2VyIn0=', '2020-05-07 05:50:30.205532'),
('nis04i1hkx5dyxd3b4gja43tp75jl78g', 'ZDE2N2FkNTI0N2NlMmNkNTBlZmUxNDhmYjRmNmJlMDc4NGNjMDFiNjp7InJvbGUiOiJVc2VyIn0=', '2020-05-07 06:37:53.913188');

-- --------------------------------------------------------

--
-- Table structure for table `landlord_land_detail`
--

CREATE TABLE `landlord_land_detail` (
  `landid` int(11) NOT NULL,
  `lattitude` double NOT NULL,
  `langitude` double NOT NULL,
  `address` varchar(255) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `city` varchar(255) NOT NULL,
  `area` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `no_of_spot` int(11) NOT NULL,
  `description` longtext DEFAULT NULL,
  `price_per_hour` double NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `userid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `landlord_land_detail`
--

INSERT INTO `landlord_land_detail` (`landid`, `lattitude`, `langitude`, `address`, `image`, `city`, `area`, `state`, `no_of_spot`, `description`, `price_per_hour`, `start_date`, `end_date`, `verified`, `userid_id`) VALUES
(2, 22.305099, 70.791384, 'Home', 'images/2020/04/22/Screenshot_261_txGUzL5.gif', 'rajkot', 'Race Course', 'Gujarat', 10, 'Best place for parking', 100, '2020-04-22', '2020-04-30', 0, 2),
(3, 22.286242, 70.808804, 'Office', 'images/2020/04/23/vacant-parking-slots-at-ballard-estate-mumbai-P7ECYE.jpg', 'rajkot', 'Gundavadi ', 'Gujarat', 20, 'For office parking', 50, '2020-04-24', '2020-05-07', 0, 4),
(4, 22.278742, 70.772471, 'Park', 'images/2020/04/23/Recycled-Rubber-Parking-Wheel-Stops-Used-in-Parking-Slots-Garages.jpg', 'rajkot', 'Mahadev Temple Garden', 'Gujarat', 18, 'Best place for parking', 40, '2020-04-23', '2020-04-29', 0, 4);

-- --------------------------------------------------------

--
-- Table structure for table `landlord_land_record`
--

CREATE TABLE `landlord_land_record` (
  `land_record_id` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `start_time` time(6) DEFAULT NULL,
  `end_time` time(6) DEFAULT NULL,
  `total_price` int(11) NOT NULL,
  `payment_remaining` tinyint(1) NOT NULL,
  `feedback` varchar(255) DEFAULT NULL,
  `landid_id` int(11) NOT NULL,
  `userid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `landlord_land_record`
--

INSERT INTO `landlord_land_record` (`land_record_id`, `start_date`, `end_date`, `start_time`, `end_time`, `total_price`, `payment_remaining`, `feedback`, `landid_id`, `userid_id`) VALUES
(1, '2020-04-23', NULL, NULL, NULL, 2400, 1, '4', 2, 1),
(2, '2020-04-28', NULL, NULL, NULL, 960, 1, '5', 4, 1),
(3, '2020-04-24', NULL, NULL, NULL, 1200, 0, '5', 3, 1),
(4, '2020-04-28', NULL, NULL, NULL, 960, 1, '4', 4, 5),
(5, '2020-04-27', NULL, NULL, NULL, 960, 1, '5', 4, 5),
(6, '2020-04-27', NULL, NULL, NULL, 960, 1, '3', 4, 5),
(7, '2020-04-26', NULL, NULL, NULL, 960, 1, '5', 4, 5),
(8, '2020-04-26', NULL, NULL, NULL, 960, 1, '5', 4, 1),
(9, '2020-04-27', NULL, NULL, NULL, 960, 1, '4', 4, 1),
(10, '2020-04-24', NULL, NULL, NULL, 960, 1, '5', 4, 1),
(11, '2020-04-28', NULL, NULL, NULL, 960, 1, '4', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user_user_detail`
--

CREATE TABLE `user_user_detail` (
  `userid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(14) NOT NULL,
  `mobile_no` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `age` int(11) NOT NULL,
  `role` varchar(10) NOT NULL,
  `otp` int(11) DEFAULT NULL,
  `face` varchar(10000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_user_detail`
--

INSERT INTO `user_user_detail` (`userid`, `name`, `password`, `mobile_no`, `email`, `age`, `role`, `otp`, `face`) VALUES
(1, 'shubham', 'shubham255', '7575880402', 'shubham@gmail.com', 19, 'User', NULL, NULL),
(2, 'yash', 'yash22', '9654854621', 'yash@gmail.com', 20, 'Landlord', NULL, NULL),
(3, 'Admin', 'admin@25', '7548962138', 'admin@gmail.com', 25, 'Admin', NULL, NULL),
(4, 'rutvik', 'rutvik02', '9876543210', 'rutvik@gmail.com', 18, 'Landlord', NULL, NULL),
(5, 'bhavya', 'bhavya21', '9874512630', 'bhavya@gmail.com', 22, 'User', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user_user_location`
--

CREATE TABLE `user_user_location` (
  `Locationid` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `lattitude` double NOT NULL,
  `langitude` double NOT NULL,
  `userid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_user_location`
--

INSERT INTO `user_user_location` (`Locationid`, `name`, `lattitude`, `langitude`, `userid_id`) VALUES
(1, 'Home', 22.226, 70.767, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `landlord_land_detail`
--
ALTER TABLE `landlord_land_detail`
  ADD PRIMARY KEY (`landid`),
  ADD KEY `Landlord_land_detail_userid_id_d0cf453f_fk_User_user` (`userid_id`);

--
-- Indexes for table `landlord_land_record`
--
ALTER TABLE `landlord_land_record`
  ADD PRIMARY KEY (`land_record_id`),
  ADD KEY `landid_index` (`landid_id`),
  ADD KEY `userid_index` (`userid_id`);

--
-- Indexes for table `user_user_detail`
--
ALTER TABLE `user_user_detail`
  ADD PRIMARY KEY (`userid`);

--
-- Indexes for table `user_user_location`
--
ALTER TABLE `user_user_location`
  ADD PRIMARY KEY (`Locationid`),
  ADD KEY `User_user_location_userid_id_14077678_fk_User_user_detail_userid` (`userid_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `landlord_land_detail`
--
ALTER TABLE `landlord_land_detail`
  MODIFY `landid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `landlord_land_record`
--
ALTER TABLE `landlord_land_record`
  MODIFY `land_record_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `user_user_detail`
--
ALTER TABLE `user_user_detail`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user_user_location`
--
ALTER TABLE `user_user_location`
  MODIFY `Locationid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `landlord_land_detail`
--
ALTER TABLE `landlord_land_detail`
  ADD CONSTRAINT `Landlord_land_detail_userid_id_d0cf453f_fk_User_user` FOREIGN KEY (`userid_id`) REFERENCES `user_user_detail` (`userid`);

--
-- Constraints for table `landlord_land_record`
--
ALTER TABLE `landlord_land_record`
  ADD CONSTRAINT `Landlord_land_record_landid_id_5bc0aac9_fk_Landlord_` FOREIGN KEY (`landid_id`) REFERENCES `landlord_land_detail` (`landid`),
  ADD CONSTRAINT `Landlord_land_record_userid_id_0c117374_fk_User_user` FOREIGN KEY (`userid_id`) REFERENCES `user_user_detail` (`userid`);

--
-- Constraints for table `user_user_location`
--
ALTER TABLE `user_user_location`
  ADD CONSTRAINT `User_user_location_userid_id_14077678_fk_User_user_detail_userid` FOREIGN KEY (`userid_id`) REFERENCES `user_user_detail` (`userid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
