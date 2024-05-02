package com.qadrqul.app.repository;

import com.qadrqul.app.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.*;

public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByNameContaining(String name);
}
