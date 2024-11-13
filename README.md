# AI-Traiding
Neural Networks in Algotraiding

## Introduction

Имея значительный опыт профессионального применения нейронных сетей в трейдинге, мы готовы поделиться материалами, не подпадающими под NDA, которые иллюстрируют наш подход к использованию ИИ на фондовом рынке. Эти материалы могут быть полезны и помочь добиться успехов тем, кто интересуется этой темой.

## Table of Contents

1. Статья: Обзор существующих подходов к торговле на фондовом рынке.
2. Статья: Структура проекта для профессионального использования нейронных сетей в трейдинге.
3. Описание подхода авторов - [pattern recognition](Pattern_recognition/ReadMe.md).:
- Статья: Анализ стационарности временных рядов и постановка задачи для pattern recognition
- Статья: Философский взгляд на поиск и распознавание паттернов
- Статья: Сравнение и выбор наиболее перспективных таймфреймов и тикеров с тз pattern recognition
- Подходы к pattern recognition с тз ИИ
- Возможные представления данных для pattern recognition при использовании нейронных сетей
4. Статистический анализ торговли созданных алгоритмов и пути улучшения результатов торговли.
5. Бэктестирование и тестирование стратегий.
6. Выводы.

___

# AI-Трейдинг: Применение Нейронных Сетей в Алготрейдинге

## Введение

Имея значительный опыт профессионального применения нейронных сетей в трейдинге, мы готовы поделиться материалами, не подпадающими под NDA, которые иллюстрируют наш подход к использованию ИИ на фондовом рынке. Эти материалы могут быть полезны и помочь добиться успехов тем, кто интересуется этой темой.

## Оглавление

1. [Введение в AI-трейдинг](#введение-в-ai-трейдинг)
    - [Почему мы используем ИИ в трейдинге?](#почему-мы-используем-ии-в-трейдинге)
    - [Почему мы используем pattern recognition в трейдинге?](#почему-мы-используем-pattern-recognition-в-трейдинге)
    - [Основные принципы и преимущества](#основные-принципы-и-преимущества)
    - [Недостатки](#недостатки)
2. [Обзор существующих подходов к торговле на фондовом рынке](#обзор-существующих-подходов)
    - [Традиционные методы](#традиционные-методы)
    - [Современные методы](#современные-методы)
3. [Основы нейронных сетей](#основы-нейронных-сетей)
    - [Типы нейронных сетей](#типы-нейронных-сетей)
    - [Архитектуры нейронных сетей](#архитектуры-нейронных-сетей)
    - [Применение нейронных сетей в трейдинге](#применение-нейронных-сетей-в-трейдинге)
4. [Анализ данных для трейдинга](#анализ-данных-для-трейдинга)
    - [Анализ стационарности временных рядов](#анализ-стационарности-временных-рядов)
    - [Методы обработки и подготовки данных](#методы-обработки-и-подготовки-данных)
5. [Распознавание паттернов в данных](#распознавание-паттернов-в-данных)
    - [Философский взгляд на поиск и распознавание паттернов](#философский-взгляд-на-поиск-и-распознавание-паттернов)
    - [Сравнение и выбор таймфреймов и тикеров](#сравнение-и-выбор-таймфреймов-и-тикеров)
    - [Методы распознавания паттернов](#методы-распознавания-паттернов)
6. [Архитектуры нейронных сетей для распознавания паттернов](#архитектуры-нейронных-сетей-для-распознавания-паттернов)
    - [Сверточные нейронные сети (CNN)](#сверточные-нейронные-сети-cnn)
    - [Рекуррентные нейронные сети (RNN)](#рекуррентные-нейронные-сети-rnn)
    - [Графовые нейронные сети (GNN)](#графовые-нейронные-сети-gnn)
    - [Гибридные модели](#гибридные-модели)
7. [Представление данных для нейронных сетей](#представление-данных-для-нейронных-сетей)
    - [Скользящие окна](#скользящие-окна)
    - [Индикаторы технического анализа](#индикаторы-технического-анализа)
    - [Комбинированные подходы](#комбинированные-подходы)
8. [Разработка и тестирование торговых алгоритмов](#разработка-и-тестирование-торговых-алгоритмов)
    - [Процесс бэктестирования](#процесс-бэктестирования)
    - [Методы оптимизации стратегий](#методы-оптимизации-стратегий)
    - [Реализация в реальных условиях](#реализация-в-реальных-условиях)
9. [Статистический анализ торговых алгоритмов](#статистический-анализ-торговых-алгоритмов)
    - [Метрики оценки эффективности](#метрики-оценки-эффективности)
    - [Анализ результатов и пути улучшения](#анализ-результатов-и-пути-улучшения)
10. [Заключение и рекомендации](#заключение-и-рекомендации)
    - [Основные выводы](#основные-выводы)
    - [Перспективы дальнейших исследований](#перспективы-дальнейших-исследований)

## Введение в AI-трейдинг

### Почему мы используем ИИ в трейдинге?
Наш подход заключается в распознавании устойчивых фигур или паттернов на рынке. Pattern recognition. 
Попытки определения паттернов обычным, алгоритмическим способом часто терпят неудачу из-за 
нестационарности временного ряда и нестабильности их формы во времени.
При этом, нейронные сети (НС) могут принимать большие объемы данных и выявлять сложные паттерны и находить "похожие", 
а не "строго одинаковые" паттерны. При этом мы говорим не о классическом ML, который использует линейные методы,
 а именно нейронные сети, способные выявлять нелинейные закономерности.

### Почему мы используем pattern recognition в трейдинге?
Позволяет избавиться от шума в данных.

### Основные принципы и преимущества
Это дает возможность уменьшать человеческий фактор в принятии решений.

### Недостатки
Плохая интерпретируемость получаемых результатов и понимание причин тех или иных решений ИИ.

## Обзор существующих подходов к торговле на фондовом рынке

### Традиционные методы
- **Технический анализ**
- **Фундаментальный анализ**

### Современные методы
- **Автоматизированные Торговые Системы (ATS)**
- **Алгоритмический трейдинг**

## Основы нейронных сетей

### Типы и архитектуры нейронных сетей
- Особенности различных типов и архитектур НС и их применение в трейдинге
- Проблема совместимости ML и бизнес-метрик

### Применение нейронных сетей в трейдинге
- Классификация и регрессия
- Распознавание паттернов

## Анализ данных для трейдинга

### Анализ стационарности временных рядов
- Методы проверки стационарности
- Выводы для финансовых временных рядов

### Методы обработки и подготовки данных
- Очистка данных
- Нормализация и стандартизация
- Иные представления данных

## Распознавание паттернов в данных [_(Patterns)_](Pattern_recognition)

### Философский взгляд на поиск и распознавание паттернов
- Что такое паттерн?
- Интуитивные методы (о чем это вообще?)
- Формализованные методы (о чем это вообще?)
- Различные подходы к разметке паттернов 
(на участках волатильности, трендах, уровнях поддержки и сопротивления и тд)
- Изменчивость паттернов во времени
- Кластеризация паттернов

### Сравнение и выбор таймфреймов и тикеров
- Анализ различных таймфреймов
- Выбор тикеров

### Методы распознавания паттернов
- Технический анализ
- Искусственный интеллект

## Архитектуры нейронных сетей для распознавания паттернов

### Сверточные нейронные сети (CNN)
- Применение к анализу графиков и ценовых данных

### Рекуррентные нейронные сети (RNN)
- Прогнозирование временных рядов

### Графовые нейронные сети (GNN)
- Применение к анализу графиков и ценовых данных

### Гибридные модели
- Сочетание различных архитектур для улучшения точности

## Представление данных для нейронных сетей

### Скользящие окна
- Создание выборок данных для обучения моделей

### Индикаторы технического анализа
- Включение различных индикаторов для улучшения качества моделей

### Комбинированные подходы
- Совмещение различных методов представления данных

## Разработка и тестирование торговых алгоритмов

### Процесс бэктестирования [_(Backtesting)_](Backtesting)
- Выбор данных
- Методы оценки
- Анализ результатов

### Методы оптимизации стратегий
- Параметрическая оптимизация
- Методы машинного обучения

### Реализация в реальных условиях
- Применение и адаптация алгоритмов в реальном времени

## Статистический анализ торговых алгоритмов

### Метрики оценки эффективности
- Доходность
- Риск
- Коэффициент Шарпа
- Максимальная просадка

### Анализ результатов и пути улучшения
- Выявление сильных и слабых сторон алгоритмов
- Рекомендации по улучшению

## Заключение и рекомендации

### Основные выводы
- Общий обзор проделанной работы

### Перспективы дальнейших исследований
- Направления для будущих исследований и разработок
- Советы для трейдеров и исследователей