$(function(){
  
  //リンクを消す
  $('#sp__bg').hide();

  //もし、.fv__hamburger（ハンバーガーボタンが）がクリックされたら...の内容を書く
  $('.fv__hamburger').click(function(){

    //もし、ハンバーガーボタンに.activeクラスが付与(hasClass)されていた場合
    if($('.fv__hamburger').hasClass('active')){

      //こちらはボタンが✕の状態の処理
      $('#sp__bg').fadeOut(300);
      $(this).removeClass('active');

      }else{

        //こちらはボタンが三本線の状態の処理
        $('#sp__bg').fadeIn(300);
        $(this).addClass('active');
      }

  });
});