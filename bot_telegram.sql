-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-02-2024 a las 19:50:25
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bot_telegram`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuncios`
--

CREATE TABLE `anuncios` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `descripcion` text NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `recompensa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `anuncios`
--

INSERT INTO `anuncios` (`id`, `titulo`, `descripcion`, `imagen`, `url`, `recompensa`) VALUES
(1, 'Anuncio 1', 'Descripción del anuncio 1', 'http://localhost/img/foto.jpg', 'https://example.com/url1', 500),
(2, 'Anuncio 2', 'Descripción del anuncio 2', 'http://localhost/img/foto.jpg', 'https://example.com/url2', 1000),
(3, 'Anuncio 3', 'Descripción del anuncio 3', 'http://localhost/img/foto.jpg', 'https://example.com/url3', 1500),
(4, 'Anuncio 1', 'Descripción del anuncio 1', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fisabellaandrespereira.neocities.org%2FTipos%2520de%2520Im%25C3%25A1genes&psig=AOvVaw0af6mQrupFLt1tbCwKt1vX&ust=1707837892922000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJiGnKyvpoQDFQAAAAAdAAAAAB', 'https://example.com/url1', 500),
(5, 'Anuncio 2', 'Descripción del anuncio 2', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fisabellaandrespereira.neocities.org%2FTipos%2520de%2520Im%25C3%25A1genes&psig=AOvVaw0af6mQrupFLt1tbCwKt1vX&ust=1707837892922000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJiGnKyvpoQDFQAAAAAdAAAAAB', 'https://example.com/url2', 1000),
(6, 'Anuncio 3', 'Descripción del anuncio 3', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fisabellaandrespereira.neocities.org%2FTipos%2520de%2520Im%25C3%25A1genes&psig=AOvVaw0af6mQrupFLt1tbCwKt1vX&ust=1707837892922000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJiGnKyvpoQDFQAAAAAdAAAAAB', 'https://example.com/url3', 1500);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` bigint(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `saldo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `saldo`) VALUES
(2147483647, 'Usuario', 0),
(6222940317, 'Usuario', 11000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `anuncios`
--
ALTER TABLE `anuncios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `anuncios`
--
ALTER TABLE `anuncios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6222940318;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
