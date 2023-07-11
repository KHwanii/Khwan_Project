package com.example.myapp.login


import com.google.gson.annotations.SerializedName
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Field
import retrofit2.http.FormUrlEncoded
import retrofit2.http.POST
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.Header

// val URL = "http://172.30.1.68:8000"
// val URL = "http://192.168.45.135:8000"
val URL = "https://management.noiroze.com"


object Login {
    val logging = HttpLoggingInterceptor().apply { level = HttpLoggingInterceptor.Level.BODY }

    val client = OkHttpClient.Builder()
        .addInterceptor(logging)
        .build()

    private val retrofit = Retrofit.Builder()
        .baseUrl(URL)
        .client(client)
        .addConverterFactory(GsonConverterFactory.create())
        .build()
    val service get() = retrofit.create(LoginService::class.java)
}

interface LoginService {
    @FormUrlEncoded
    @POST("/api/user_login/")
    suspend fun userLogin(                      // 로그인을 처리하는 함수
        @Field("userid") userid: String,
        @Field("password") password: String
    ): Response<LoginUser> // 서버로부터 응답을 받고, LoginUser 데이터 클래스에 데이터를 저장.

    @GET("/api/user_detail/")
    suspend fun getUserDetail(
        @Header("Authorization") token: String
    ): Response<UserDetail>
}

data class User(                      // http://IP주소/api/user_login/ 에서 받아오는 데이터 형식
    @SerializedName("count")
    val count: Int,
    @SerializedName("next")
    val next: String,
    @SerializedName("previous")
    val previous: String,
    @SerializedName("results")
    val results: List<LoginUser>        // results 안의 데이터가 실제 데이터. 리스트 형태로 받아서 Result 데이터 클래스에 집어넣음
)

data class LoginUser(                // 받아오는 각각의 로그인 성공 한 User 데이터들
    @SerializedName("userid")
    val userid: String,
    @SerializedName("token")
    val token: String,
    @SerializedName("dong")
    val dong: String,
    @SerializedName("ho")
    val ho: String,
)


data class UserDetail(
    @SerializedName("userid")
    val userid: String,
    @SerializedName("dong")
    val dong: String,
    @SerializedName("ho")
    val ho: String,
    // 필요하면 나머지 필드도 추가
)