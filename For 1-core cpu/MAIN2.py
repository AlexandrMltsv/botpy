﻿from threading import Thread
import Server , CONFIG
thread_vk_bot_resend = Thread(target=Server.vk_bot_resend,args=())
thread_vk_bot_resend.start()
thread_vk_bot_resend.join()
Server.vk.messages.send(random_id=Server.random.randint(0, 999999), message=f"WARNING : " 
                                                                            f"{CONFIG.users_list_warn}"
                                                                            " Поток-RESEND уничтожен",
                                                                    peer_id=CONFIG.PEER_CRUSH_EVENT)