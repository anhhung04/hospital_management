function Header() {
  return (
    <header>
      <div class="w-full h-1/6 px-[51px] py-[51px] border-b-[1px] flex items-center justify-between">
        <div class="flex flex-grow">
          <img src="/images/image.png" alt="logo" class="w-[112px] h-[57px]" />
        </div>
        <button class="w-[177px] h-[36px] rounded-2xl text-[#110BBF] font-semibold hover:text-[#000000] text-xl">Đăng Nhập</button>
      </div>
    </header>
  );
}

export default Header;
