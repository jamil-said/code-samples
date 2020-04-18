<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Users;

class ApiController extends Controller
{
    public function getAllUsers() {
        $users = Users::get()->toJson(JSON_PRETTY_PRINT);
        return response($users, 200);
    }

    public function createUser(Request $request) {
        if (empty($request->first_name) || empty($request->last_name) || empty($request->email)){
            return response()->json([
                "message" => "Request failed! The fiels 'First Name', 'Last Name' and 'Email' must be all provided for user creation."
            ], 400);
        }
        if (strlen($request->first_name) > 100 || strlen($request->last_name) > 100 || strlen($request->email) > 100){
            return response()->json([
                "message" => "Request failed! The fiels 'First Name', 'Last Name' and 'Email' must each have a maximum of 100 characters."
            ], 400);
        }
        if (Users::where('email', $request->email)->exists()) {
            return response()->json([
                "message" => "Request failed! The email provided is already in use."
            ], 400);            
        }
        $users = new Users;
        $users->first_name = $request->first_name;
        $users->last_name = $request->last_name;
        $users->email = $request->email;
        $users->save();
        return response()->json([
            "message" => "User record created"
        ], 201);
    }

    public function updateUser(Request $request, $id) {
        if (empty($request->first_name) && empty($request->last_name) && empty($request->email)){
            return response()->json([
                "message" => "Request failed! At least one field to be updated must be provided"
            ], 400);
        }
        if ((!empty($request->first_name) && strlen($request->first_name) > 100) || 
        (!empty($request->last_name) && strlen($request->last_name) > 100) || 
        (!empty($request->email) && strlen($request->email) > 100)){
            return response()->json([
                "message" => "Request failed! The fiels 'First Name', 'Last Name' and 'Email' must each have a maximum of 100 characters."
            ], 400);
        }
        if (!empty($request->email)){
            if (Users::where('email', $request->email)->exists()) {
                return response()->json([
                    "message" => "Request failed! The email provided is already in use."
                ], 400);            
            }
        }
        if (Users::where('id', $id)->exists()) {
            $user = Users::find($id);
            $user->first_name = empty($request->first_name) ? $user->first_name : $request->first_name;
            $user->last_name = empty($request->last_name) ? $user->last_name : $request->last_name;
            $user->email = empty($request->email) ? $user->email : $request->email;
            $user->save();
            return response()->json([
                "message" => "Request processed successfully"
            ], 200);
            } else {
            return response()->json([
                "message" => "User not found"
            ], 404);
        }
    }    
    
    public function deleteUser ($id) {
        if (Users::where('id', $id)->exists()) {
            $user = Users::find($id);
            $user->delete();
            return response()->json([
              "message" => "User record deleted"
            ], 200);
            } else {
            return response()->json([
              "message" => "User not found"
            ], 404);
        }
    }
    
}
