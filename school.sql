-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 01-Jun-2020 às 18:41
-- Versão do servidor: 10.4.11-MariaDB
-- versão do PHP: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `school`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `classes`
--

CREATE TABLE `classes` (
  `class_id` int(30) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `classes`
--

INSERT INTO `classes` (`class_id`, `name`) VALUES
(1, 'Economy 101'),
(2, 'English 1.0'),
(3, 'English 2.0'),
(4, 'English 3.0'),
(5, 'Global Economy'),
(6, 'Introduction to pragramming');

-- --------------------------------------------------------

--
-- Estrutura da tabela `professor`
--

CREATE TABLE `professor` (
  `ssn_professor` int(30) NOT NULL,
  `name` varchar(255) NOT NULL,
  `pass_access` varchar(25) NOT NULL,
  `phone` int(13) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `id_class` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `professor`
--

INSERT INTO `professor` (`ssn_professor`, `name`, `pass_access`, `phone`, `email`, `id_class`) VALUES
(123, 'Alex Dangerous', '12345a', 283823, 'Alex12', 3),
(1234, 'Victor Baracho', '123456', 123123, 'victor123@university.com', 1),
(12343, 'Alejandro Balsas', '123456', 123123, 'alejandro@university.com', 3),
(123433, 'BIllboard Awards', '12314123', 1231123, 'billboard@univertisy.com', 1),
(11231231, 'Alex Gane', 'abc@22', 8877377, 'alexgane@university.com', 1),
(123123321, 'Júlio Sterblitz', '123@@bb', 2147483647, 'julio@university.com', 3),
(188923882, 'Heitor Arlif', '234@bb', 2147483647, 'heitor@university.com', 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `student`
--

CREATE TABLE `student` (
  `ssn_student` int(30) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` int(13) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pass_access` varchar(25) NOT NULL,
  `id_class` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `student`
--

INSERT INTO `student` (`ssn_student`, `name`, `phone`, `email`, `pass_access`, `id_class`) VALUES
(1, 'Bou', 123, 'aa', '123456', 1),
(2, 'Ban', 123, 'ab', '123456', 3),
(123, 'Ellen Degeneres', 12939123, 'ellen@university.com', '12312a', 4),
(12311, 'Jax', 12312, 'Jax', '123456', 3),
(1211111, 'Jambo', 1231, 'Jambo', '123456', 3),
(12312412, 'Birror Jake', 1231412, 'birror@university.com', 'asadas', 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `student_notes`
--

CREATE TABLE `student_notes` (
  `ssn_student` int(30) NOT NULL,
  `first_quarter` decimal(3,1) DEFAULT NULL,
  `second_quarter` decimal(3,1) DEFAULT NULL,
  `third_quarter` decimal(3,1) DEFAULT NULL,
  `fourth_quarter` decimal(3,1) DEFAULT NULL,
  `id_class` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `student_notes`
--

INSERT INTO `student_notes` (`ssn_student`, `first_quarter`, `second_quarter`, `third_quarter`, `fourth_quarter`, `id_class`) VALUES
(1, '10.0', '5.5', '10.0', '9.0', 2),
(123, '0.0', '0.0', '0.0', '0.0', 1),
(12311, NULL, NULL, NULL, NULL, 3),
(1211111, NULL, NULL, NULL, NULL, 3),
(12312412, '10.0', '7.1', '9.0', '10.0', 2);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`class_id`);

--
-- Índices para tabela `professor`
--
ALTER TABLE `professor`
  ADD PRIMARY KEY (`ssn_professor`),
  ADD KEY `id_class` (`id_class`);

--
-- Índices para tabela `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`ssn_student`),
  ADD KEY `id_class` (`id_class`);

--
-- Índices para tabela `student_notes`
--
ALTER TABLE `student_notes`
  ADD PRIMARY KEY (`ssn_student`),
  ADD KEY `id_class` (`id_class`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `classes`
--
ALTER TABLE `classes`
  MODIFY `class_id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `professor`
--
ALTER TABLE `professor`
  ADD CONSTRAINT `professor_ibfk_1` FOREIGN KEY (`id_class`) REFERENCES `classes` (`class_id`);

--
-- Limitadores para a tabela `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`id_class`) REFERENCES `classes` (`class_id`);

--
-- Limitadores para a tabela `student_notes`
--
ALTER TABLE `student_notes`
  ADD CONSTRAINT `student_notes_ibfk_1` FOREIGN KEY (`ssn_student`) REFERENCES `student` (`ssn_student`),
  ADD CONSTRAINT `student_notes_ibfk_2` FOREIGN KEY (`id_class`) REFERENCES `classes` (`class_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
