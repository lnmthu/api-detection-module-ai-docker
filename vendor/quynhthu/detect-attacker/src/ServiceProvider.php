<?php

namespace quynhthu\DetectAttacker;

class ServiceProvider extends \Illuminate\Support\ServiceProvider
{
    const CONFIG_PATH = __DIR__ . '/../config/detect-attacker.php';

    public function boot()
    {
        $this->publishes([
            self::CONFIG_PATH => config_path('detect-attacker.php'),
        ], 'config');

    }

    public function register()
    {
        $this->mergeConfigFrom(
            self::CONFIG_PATH,
            'detect-attacker'
        );
    }
}
