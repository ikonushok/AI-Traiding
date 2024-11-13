# Обоснование подхода к распознаванию паттернов в цифровых рядах (на примере трейдинга)

## Раздел I. Введение
1. Нестационарность временных рядов и что это означает для pattern-recognition
2. Изменчивость паттернов во времени
3. Гипотеза: можно обучить нейронную сеть (НС) так, чтобы она распознавала видоизмененные паттерны с точностью, достаточной для постоения прибыльно Торговой системы (ТС)

## Раздел II. План исследования
1. Предмет исследования
2. Сбор датасета: варианты разметки паттернов, после которых следует рост или падение цены
   1. нахождение экстремумов
   2. уровни поддержки и сопротивления
   3. ...
3. Изучение их изменяемости во времени
4. Кластеризация паттернов, как попытка найти общие формы для похожих паттернов
5. Создание алгоритма. Схема пайплайна для эксперимента
   1. dataset
   2. preprocessing
   3. nn model
   4. training
   5. validation
   6. test
   7. backtesting, как инструмент тестирования результатов обученной НС. Переход от ML метрик к бизнес-метрикам.
6. Оценка эффективности алгоритма. Интерпретация результатов. Подготовка для следующих исследований

## Раздел III. Эксперимент
1. Подготовка датасета
2. Подготовка различных нейронных сетей
3. Обучение нейронных сетей и проверка на тестовой выборке
4. Оценка эффективности алгоритмов с тз трейдинга
5. Интерпретация результатов. Подготовка для следующих исследований

## Раздел IV. Возможные направления будущих исследований
1. Различные архитектуры НС:
   1. применение графовых сетей, как способ анализа связей между временными рядами
   2. attention
   3. ...
2. Изучение влияния feature engineering в подходе pattern recognition: 
   1. logdiff
   2. замена OHCLV на technical indicators
   3. спектральное представление паттерна
3. Прочие подходы к использованию ИИ в трейдинге