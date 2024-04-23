-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: May 23, 2020 at 04:28 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `citywebsite_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add camera_ circle', 1, 'add_camera_circle'),
(2, 'Can change camera_ circle', 1, 'change_camera_circle'),
(3, 'Can delete camera_ circle', 1, 'delete_camera_circle'),
(4, 'Can view camera_ circle', 1, 'view_camera_circle'),
(5, 'Can add camera_ city', 2, 'add_camera_city'),
(6, 'Can change camera_ city', 2, 'change_camera_city'),
(7, 'Can delete camera_ city', 2, 'delete_camera_city'),
(8, 'Can view camera_ city', 2, 'view_camera_city'),
(9, 'Can add camera_ name', 3, 'add_camera_name'),
(10, 'Can change camera_ name', 3, 'change_camera_name'),
(11, 'Can delete camera_ name', 3, 'delete_camera_name'),
(12, 'Can view camera_ name', 3, 'view_camera_name'),
(13, 'Can add camera_ state', 4, 'add_camera_state'),
(14, 'Can change camera_ state', 4, 'change_camera_state'),
(15, 'Can delete camera_ state', 4, 'delete_camera_state'),
(16, 'Can view camera_ state', 4, 'view_camera_state'),
(17, 'Can add user_ role', 5, 'add_user_role'),
(18, 'Can change user_ role', 5, 'change_user_role'),
(19, 'Can delete user_ role', 5, 'delete_user_role'),
(20, 'Can view user_ role', 5, 'view_user_role'),
(21, 'Can add user_ signup', 6, 'add_user_signup'),
(22, 'Can change user_ signup', 6, 'change_user_signup'),
(23, 'Can delete user_ signup', 6, 'delete_user_signup'),
(24, 'Can view user_ signup', 6, 'view_user_signup'),
(25, 'Can add user_ complain', 7, 'add_user_complain'),
(26, 'Can change user_ complain', 7, 'change_user_complain'),
(27, 'Can delete user_ complain', 7, 'delete_user_complain'),
(28, 'Can view user_ complain', 7, 'view_user_complain'),
(29, 'Can add report_ details', 8, 'add_report_details'),
(30, 'Can change report_ details', 8, 'change_report_details'),
(31, 'Can delete report_ details', 8, 'delete_report_details'),
(32, 'Can view report_ details', 8, 'view_report_details'),
(33, 'Can add log entry', 9, 'add_logentry'),
(34, 'Can change log entry', 9, 'change_logentry'),
(35, 'Can delete log entry', 9, 'delete_logentry'),
(36, 'Can view log entry', 9, 'view_logentry'),
(37, 'Can add permission', 10, 'add_permission'),
(38, 'Can change permission', 10, 'change_permission'),
(39, 'Can delete permission', 10, 'delete_permission'),
(40, 'Can view permission', 10, 'view_permission'),
(41, 'Can add group', 11, 'add_group'),
(42, 'Can change group', 11, 'change_group'),
(43, 'Can delete group', 11, 'delete_group'),
(44, 'Can view group', 11, 'view_group'),
(45, 'Can add user', 12, 'add_user'),
(46, 'Can change user', 12, 'change_user'),
(47, 'Can delete user', 12, 'delete_user'),
(48, 'Can view user', 12, 'view_user'),
(49, 'Can add content type', 13, 'add_contenttype'),
(50, 'Can change content type', 13, 'change_contenttype'),
(51, 'Can delete content type', 13, 'delete_contenttype'),
(52, 'Can view content type', 13, 'view_contenttype'),
(53, 'Can add session', 14, 'add_session'),
(54, 'Can change session', 14, 'change_session'),
(55, 'Can delete session', 14, 'delete_session'),
(56, 'Can view session', 14, 'view_session');

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `camera_circle`
--

CREATE TABLE `camera_circle` (
  `circle_id` int(11) NOT NULL,
  `circle_name` varchar(40) NOT NULL,
  `city_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `camera_circle`
--

INSERT INTO `camera_circle` (`circle_id`, `circle_name`, `city_id`) VALUES
(1, 'abcd', 1),
(2, 'wxyz', 2);

-- --------------------------------------------------------

--
-- Table structure for table `camera_city`
--

CREATE TABLE `camera_city` (
  `city_id` int(11) NOT NULL,
  `city_name` varchar(40) NOT NULL,
  `state_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `camera_city`
--

INSERT INTO `camera_city` (`city_id`, `city_name`, `state_id`) VALUES
(1, 'abc', 1),
(2, 'xyz', 2);

-- --------------------------------------------------------

--
-- Table structure for table `camera_name`
--

CREATE TABLE `camera_name` (
  `camera_id` int(11) NOT NULL,
  `camera_name` varchar(40) NOT NULL,
  `camera_ip_addr` varchar(30) NOT NULL,
  `camera_status` int(11) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `circle_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `camera_name`
--

INSERT INTO `camera_name` (`camera_id`, `camera_name`, `camera_ip_addr`, `camera_status`, `created_date`, `updated_date`, `circle_id`) VALUES
(1, 'cam-1', '127.0.6.7', 1, '2020-05-21 00:00:00.000000', '2020-05-22 00:00:00.000000', 1),
(2, 'cam-2', '127.1.3.5', 1, '2020-05-22 00:00:00.000000', '2020-05-22 00:00:00.000000', 2);

-- --------------------------------------------------------

--
-- Table structure for table `camera_state`
--

CREATE TABLE `camera_state` (
  `state_id` int(11) NOT NULL,
  `state_name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `camera_state`
--

INSERT INTO `camera_state` (`state_id`, `state_name`) VALUES
(1, 'gujarat'),
(2, 'maharastra');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(9, 'admin', 'logentry'),
(11, 'auth', 'group'),
(10, 'auth', 'permission'),
(12, 'auth', 'user'),
(1, 'CityWebsite', 'camera_circle'),
(2, 'CityWebsite', 'camera_city'),
(3, 'CityWebsite', 'camera_name'),
(4, 'CityWebsite', 'camera_state'),
(8, 'CityWebsite', 'report_details'),
(7, 'CityWebsite', 'user_complain'),
(5, 'CityWebsite', 'user_role'),
(6, 'CityWebsite', 'user_signup'),
(13, 'contenttypes', 'contenttype'),
(14, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'CityWebsite', '0001_initial', '2020-05-23 13:09:45.379530'),
(2, 'contenttypes', '0001_initial', '2020-05-23 13:09:50.159677'),
(3, 'auth', '0001_initial', '2020-05-23 13:09:52.738946'),
(4, 'admin', '0001_initial', '2020-05-23 13:10:00.785821'),
(5, 'admin', '0002_logentry_remove_auto_add', '2020-05-23 13:10:02.629167'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2020-05-23 13:10:02.707245'),
(7, 'contenttypes', '0002_remove_content_type_name', '2020-05-23 13:10:04.097580'),
(8, 'auth', '0002_alter_permission_name_max_length', '2020-05-23 13:10:05.019278'),
(9, 'auth', '0003_alter_user_email_max_length', '2020-05-23 13:10:06.597031'),
(10, 'auth', '0004_alter_user_username_opts', '2020-05-23 13:10:06.721973'),
(11, 'auth', '0005_alter_user_last_login_null', '2020-05-23 13:10:07.270205'),
(12, 'auth', '0006_require_contenttypes_0002', '2020-05-23 13:10:07.322396'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2020-05-23 13:10:07.393753'),
(14, 'auth', '0008_alter_user_username_max_length', '2020-05-23 13:10:08.051662'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2020-05-23 13:10:08.817069'),
(16, 'auth', '0010_alter_group_name_max_length', '2020-05-23 13:10:09.770004'),
(17, 'auth', '0011_update_proxy_permissions', '2020-05-23 13:10:09.879318'),
(18, 'sessions', '0001_initial', '2020-05-23 13:10:10.332358');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('nz3d54jmtjqgu9vk6yh9nyjs85wxgxie', 'Y2MwMDk4OGYzZDE0Y2Y0MjE2NGExZGRjZmMyMDAwOGViODc0MmEzZjp7ImlkIjoyLCJmaXJzdF9uYW1lIjoiVmlzaHYgIFBhdGVsIiwicm9sZSI6ImVtcGxveWVlIiwicGhvdG8iOiJibGFua191c2VyLnBuZyJ9', '2020-06-06 14:22:01.592796');

-- --------------------------------------------------------

--
-- Table structure for table `report_details`
--

CREATE TABLE `report_details` (
  `report_id` int(11) NOT NULL,
  `generated_date` datetime(6) NOT NULL,
  `garbage_detection` int(11) NOT NULL,
  `pothole_detection` int(11) NOT NULL,
  `hand_gesture_detection` int(11) NOT NULL,
  `captured_image` varchar(500) NOT NULL,
  `scanned_image` varchar(500) NOT NULL,
  `report_status` int(11) NOT NULL,
  `camera_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_complain`
--

CREATE TABLE `user_complain` (
  `complain_id` int(11) NOT NULL,
  `uploaded_image` varchar(500) NOT NULL,
  `description` varchar(500) NOT NULL,
  `address` varchar(500) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `solved_date` datetime(6) DEFAULT NULL,
  `complain_status` int(11) NOT NULL,
  `deduction_points` int(11) NOT NULL,
  `city_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_role`
--

CREATE TABLE `user_role` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_role`
--

INSERT INTO `user_role` (`role_id`, `role_name`) VALUES
(1, 'super admin'),
(2, 'admin'),
(3, 'employee'),
(4, 'citizen'),
(5, 'technician');

-- --------------------------------------------------------

--
-- Table structure for table `user_signup`
--

CREATE TABLE `user_signup` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `password` varchar(500) NOT NULL,
  `email` varchar(70) NOT NULL,
  `aadhar_card` varchar(14) NOT NULL,
  `contact_no` bigint(20) DEFAULT NULL,
  `created_date` datetime(6) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `user_status` int(11) NOT NULL,
  `complain_points` int(11) NOT NULL,
  `profile_photo` varchar(500) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `otp_used` int(11) DEFAULT NULL,
  `otp_email` varchar(10) DEFAULT NULL,
  `is_valid` int(11) DEFAULT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_signup`
--

INSERT INTO `user_signup` (`user_id`, `first_name`, `last_name`, `password`, `email`, `aadhar_card`, `contact_no`, `created_date`, `updated_date`, `user_status`, `complain_points`, `profile_photo`, `otp`, `otp_used`, `otp_email`, `is_valid`, `role_id`) VALUES
(1, 'Rutvij', 'Bhatt', '81dc9bdb52d04dc20036dbd8313ed055', 'rutvijbhatt207@gmail.com', '123456789012', 9563245896, '2020-05-17 06:10:00.000000', '2020-05-23 13:58:13.423607', 1, 100, '2.jpg', NULL, NULL, NULL, 1, 1),
(2, 'Vishv ', 'Patel', '674f3c2c1a8a6f90461e8a66fb5550ba', 'vishvpatel@engineer.com', '789654123569', 8956741235, '2020-05-19 05:00:00.000000', '2020-05-21 05:12:25.478000', 1, 100, 'blank_user.png', NULL, NULL, NULL, 1, 3);

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
-- Indexes for table `camera_circle`
--
ALTER TABLE `camera_circle`
  ADD PRIMARY KEY (`circle_id`),
  ADD KEY `camera_circle_city_id_30c9679e_fk_camera_city_city_id` (`city_id`);

--
-- Indexes for table `camera_city`
--
ALTER TABLE `camera_city`
  ADD PRIMARY KEY (`city_id`),
  ADD KEY `camera_city_state_id_fc8eaa13_fk_camera_state_state_id` (`state_id`);

--
-- Indexes for table `camera_name`
--
ALTER TABLE `camera_name`
  ADD PRIMARY KEY (`camera_id`),
  ADD UNIQUE KEY `camera_ip_addr` (`camera_ip_addr`),
  ADD KEY `camera_name_circle_id_60d57f41_fk_camera_circle_circle_id` (`circle_id`);

--
-- Indexes for table `camera_state`
--
ALTER TABLE `camera_state`
  ADD PRIMARY KEY (`state_id`);

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
-- Indexes for table `report_details`
--
ALTER TABLE `report_details`
  ADD PRIMARY KEY (`report_id`),
  ADD KEY `report_details_camera_id_6e61ef5a_fk_camera_name_camera_id` (`camera_id`);

--
-- Indexes for table `user_complain`
--
ALTER TABLE `user_complain`
  ADD PRIMARY KEY (`complain_id`),
  ADD KEY `user_complain_city_id_06e8bb0c_fk_camera_city_city_id` (`city_id`),
  ADD KEY `user_complain_user_id_040c134a_fk_user_signup_user_id` (`user_id`);

--
-- Indexes for table `user_role`
--
ALTER TABLE `user_role`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `user_signup`
--
ALTER TABLE `user_signup`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `aadhar_card` (`aadhar_card`),
  ADD KEY `user_signup_role_id_d364f4b6_fk_user_role_role_id` (`role_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

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
-- AUTO_INCREMENT for table `camera_circle`
--
ALTER TABLE `camera_circle`
  MODIFY `circle_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `camera_city`
--
ALTER TABLE `camera_city`
  MODIFY `city_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `camera_name`
--
ALTER TABLE `camera_name`
  MODIFY `camera_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `camera_state`
--
ALTER TABLE `camera_state`
  MODIFY `state_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `report_details`
--
ALTER TABLE `report_details`
  MODIFY `report_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_complain`
--
ALTER TABLE `user_complain`
  MODIFY `complain_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_role`
--
ALTER TABLE `user_role`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user_signup`
--
ALTER TABLE `user_signup`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
-- Constraints for table `camera_circle`
--
ALTER TABLE `camera_circle`
  ADD CONSTRAINT `camera_circle_city_id_30c9679e_fk_camera_city_city_id` FOREIGN KEY (`city_id`) REFERENCES `camera_city` (`city_id`);

--
-- Constraints for table `camera_city`
--
ALTER TABLE `camera_city`
  ADD CONSTRAINT `camera_city_state_id_fc8eaa13_fk_camera_state_state_id` FOREIGN KEY (`state_id`) REFERENCES `camera_state` (`state_id`);

--
-- Constraints for table `camera_name`
--
ALTER TABLE `camera_name`
  ADD CONSTRAINT `camera_name_circle_id_60d57f41_fk_camera_circle_circle_id` FOREIGN KEY (`circle_id`) REFERENCES `camera_circle` (`circle_id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `report_details`
--
ALTER TABLE `report_details`
  ADD CONSTRAINT `report_details_camera_id_6e61ef5a_fk_camera_name_camera_id` FOREIGN KEY (`camera_id`) REFERENCES `camera_name` (`camera_id`);

--
-- Constraints for table `user_complain`
--
ALTER TABLE `user_complain`
  ADD CONSTRAINT `user_complain_city_id_06e8bb0c_fk_camera_city_city_id` FOREIGN KEY (`city_id`) REFERENCES `camera_city` (`city_id`),
  ADD CONSTRAINT `user_complain_user_id_040c134a_fk_user_signup_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_signup` (`user_id`);

--
-- Constraints for table `user_signup`
--
ALTER TABLE `user_signup`
  ADD CONSTRAINT `user_signup_role_id_d364f4b6_fk_user_role_role_id` FOREIGN KEY (`role_id`) REFERENCES `user_role` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
