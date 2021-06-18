
FROM thuicetea/module_detection:version-model-final-one

# USER root

# WORKDIR /var/www/html

# RUN apt-get update && apt-get install -y \
#         libpng-dev \
#         zlib1g-dev \
#         libxml2-dev \
#         libzip-dev \
#         libonig-dev \
#         zip \
#         curl \
#         unzip \
#     && docker-php-ext-configure gd \
#     && docker-php-ext-install -j$(nproc) gd \
#     && docker-php-ext-install pdo_mysql \
#     && docker-php-ext-install mysqli \
#     && docker-php-ext-install zip \
#     && docker-php-source delete

# COPY .docker/vhost.conf /etc/apache2/sites-available/000-default.conf

COPY . /var/www/html

# RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# RUN apt install -y python3 python3.pip
# RUN pip3 install --upgrade pip
# RUN pip3 install --upgrade setuptools pip
# RUN pip3 install numpy
# RUN pip3 install pandas
# RUN apt install -y python3-opencv
# RUN pip3 install keras
# RUN pip3 install  --upgrade tensorflow

RUN chown -R www-data:www-data /var/www/html \
    && a2enmod rewrite


