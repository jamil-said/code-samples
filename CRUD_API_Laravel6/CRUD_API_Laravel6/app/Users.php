<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Users extends Model
{
    protected $table = 'apiusers';
    protected $fillable = ['first_name', 'last_name', 'email'];
}
